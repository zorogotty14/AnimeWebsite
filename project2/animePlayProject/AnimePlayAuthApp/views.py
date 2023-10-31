from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from AnimePlayApp.models import *
from AnimePlayApp.views import *
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":

        user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])

        login(request, user)

        return render(request, "AnimePlayApp/watchlist.html")

    else:
        return render(request, "AnimePlayAuthApp/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if( (username == new_User['username']) and (password == new_User['password'])):
            request.session['username'] = username
            request.session['role'] = 'regular'
            subcategory_data = json['category'][0]['recommendations']
            return render(request, 'AnimePlayApp/watchlist.html', {'subcategory_data': subcategory_data, 'subcategory': 'recommendations'})
        else:
            return redirect('/')

    else:
        return render(request, "AnimePlayAuthApp/login.html")

def logout_view(request):
    del request.session['username']
    del request.session['role']
    logout(request)
    return redirect('/')