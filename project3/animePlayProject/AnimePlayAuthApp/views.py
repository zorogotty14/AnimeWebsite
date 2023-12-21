from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from AnimePlayApp.models import *
from AnimePlayApp.views import *
from AnimePlayApp.forms import SearchForm
from django.http import HttpResponse
from AnimePlayActionsApp.models import *
from . import forms


# Create your views here.

# register the users
def register_view(request):
    form = forms.SignUp()
    if request.method == "POST":
        #processing the forms
        form = forms.SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #creating the User with required field
            user = User.objects.create_user(username, email, password)
            login(request, user)
            #adding sessions
            request.session['username'] = username
            request.session['role'] = 'regular'
            # adding messages
            verb = "created the profile "+username
            actions = Action(
                user=user,
                verb=verb,
                target=user
            )
            actions.save()
            messages.add_message(request, messages.SUCCESS, f'Hi {username} your account has been created')
            user = User.objects.get(username=username)
            user.details.role = 'regular'
            user.save()
            return redirect('/')
        else:
            searchform = SearchForm()
            return render(request, "AnimePlayAuthApp/register.html", {'form': form, 'searchform':searchform})
    else:
        searchform = SearchForm()
        return render(request, "AnimePlayAuthApp/register.html", {'form': form, 'searchform':searchform})

#login User function
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        #checking if user is not none
        if user is not None:
            request.session['username'] = user.username
            request.session['role'] = user.details.role
            messages.add_message(request, messages.INFO, f'Hi {username},Welcome to our site')
            login(request, user)
        else:
            #anyerrors found displaying the errors
            messages.add_message(request, messages.ERROR, 'username or password incorrect please try again')
            form = SearchForm()
            return render(request, "AnimePlayAuthApp/login.html",{'form':form})
        return redirect('/')
    else:
        #displaying the empty login forms
        form = SearchForm()
        return render(request, "AnimePlayAuthApp/login.html",{'form': form})

#logout forms
def logout_view(request):
    username = request.session['username']
    del request.session['username']
    del request.session['role']
    logout(request)
    messages.add_message(request, messages.INFO, 'User '+username+' logged out')
    return redirect('/')

#view the profile page
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    activities = Action.objects.filter(user_id=user.id,
                                       target_ct=ContentType.objects.get_for_model(user))
    activities = activities.order_by('-created')[:10]
    form = SearchForm()
    return render(request, 'AnimePlayAuthApp/profile.html', {
        'user': user,
        'activities':activities,
        'form': form
    })
#edit the profile page
def profile_edit(request,username):
    if request.method == "POST":
        user = User.objects.get(username=username)
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        #only admin has access to edit the role, other aspects like name, email each user can perform
        if( request.user.id == user.id):
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.details.role = 'regular'
            user.save()
            verb = "edited the profile " + firstname + " "+ lastname +" "+user.username
            actions = Action(
                user=request.user,
                verb=verb,
                target=user
            )
            actions.save()
            messages.add_message(request, messages.INFO, f'Profile details has been changed')
            return redirect('/auth/profile/'+str(username))
        elif request.user.is_superuser:
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.details.role = request.POST['role']
            user.save()
            verb = "edited the profile " + firstname + " " + lastname + " " +user.username
            actions = Action(
                user=request.user,
                verb=verb,
                target=user
            )
            actions.save()
            messages.add_message(request, messages.INFO, f'Profile details has been changed')
            return redirect('/auth/profile/' + str(username))
        else:
            messages.add_message(request, messages.WARNING, f'you are not authorised to change profile details')
            return redirect('/auth/profile/' + str(username))
    else:
        user = get_object_or_404(User, username=username)
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/editprofile.html',{
            'users_profile': user,
            'form': form
        })
#delete the profile only admin has access
def profile_del(request,username):
    if request.method == "POST" and request.user.is_superuser:
        user = User.objects.get(username=username)
        username1 = user.username
        verb = "Deleted the user " + username1
        actions = Action(
            user=user,
            verb=verb,
            target=user
        )
        actions.save()
        user.delete()
        messages.add_message(request, messages.WARNING, f'Profile '+username1+' has been deleted')
        return redirect('/')
    else:
        messages.add_message(request, messages.WARNING, f'you dont have access to delete profiles')
        return redirect('/')
