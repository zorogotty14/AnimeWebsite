from django.shortcuts import *
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm, AddAnimeForm, DeleteAnimeForm, NewCommentForm# Import your SearchForm
from AnimePlayActionsApp.models import *
from django_ratelimit.decorators import ratelimit
import requests



#home page listing all the categories
def index(request):
    user = request.user.is_authenticated
    if user:
        #getting all data from database
        list_anime = Anime.objects.all()
        list_category = AnimeCategory.objects.all()
        friends_activities = Action.objects.all()
        activities = friends_activities
        activities = activities.order_by('-created')[:10]
        form = SearchForm()
        context = {
            'list_anime': list_anime,
            'list_category': list_category,
            'activities' : activities,
            'form': form
        }
        return render(request, 'AnimePlayApp/index.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# category page for movies
@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def movies(request):
    user = request.user.is_authenticated
    if user:
        list_anime = Anime.objects.order_by('name').filter(type='movies').values()
        url = "https://myanimelist.p.rapidapi.com/anime/top/movie"

        headers = {
            "X-RapidAPI-Key": "0a0b72559emshc1ca09f720d7505p15e229jsnfcf4f42dc10a",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }
        data = None
        try:
            response = requests.get(url, headers=headers)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Handle the successful response
                data = response.json()
                # Process the data as needed
            else:
                # Handle other HTTP status codes (e.g., 404 Not Found, 500 Internal Server Error)
                messages.add_message(request, messages.ERROR,
                                     f"API request failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Handle general request exceptions (e.g., network issues)
            messages.add_message(request, messages.ERROR, "API request failed with exception:",
                                 e)
        except ratelimit.Ratelimited as e:
            messages.add_message(request, messages.ERROR, "Rate limit exceeded. Please try again later.",
                                 e)
            # Handle rate limit exceedance
            return HttpResponse("Rate limit exceeded. Please try again later.", status=429)
        except Exception as e:
            # Handle other unexpected exceptions
            messages.add_message(request, messages.ERROR, "An unexpected error occurred:",
                                 e)
        form = SearchForm()
        context = {
            'response': data,
            'list_anime': list_anime,
            'subcategory': 'movies',
            'form':form
        }
        return render(request, 'AnimePlayApp/category.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# category page for series
@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def series(request):
    user = request.user.is_authenticated
    if user:
        list_anime = Anime.objects.order_by('name').filter(type='series').values()
        url = "https://myanimelist.p.rapidapi.com/anime/top/tv"

        headers = {
            "X-RapidAPI-Key": "0a0b72559emshc1ca09f720d7505p15e229jsnfcf4f42dc10a",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }
        data = None
        try:
            response = requests.get(url, headers=headers)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Handle the successful response
                data = response.json()
                # Process the data as needed
            else:
                # Handle other HTTP status codes (e.g., 404 Not Found, 500 Internal Server Error)
                messages.add_message(request, messages.ERROR,
                                     f"API request failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Handle general request exceptions (e.g., network issues)
            messages.add_message(request, messages.ERROR, "API request failed with exception:",
                                 e)
        except ratelimit.Ratelimited as e:
            messages.add_message(request, messages.ERROR, "Rate limit exceeded. Please try again later.",
                                 e)
            # Handle rate limit exceedance
            return HttpResponse("Rate limit exceeded. Please try again later.", status=429)
        except Exception as e:
            # Handle other unexpected exceptions
            messages.add_message(request, messages.ERROR, "An unexpected error occurred:",
                                 e)
        form = SearchForm()
        context = {
            'response': data,
            'list_anime': list_anime,
            'subcategory': 'series',
            'form': form
        }
        return render(request, 'AnimePlayApp/category.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# category page for recommendations
@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def recom(request):
    user = request.user.is_authenticated
    if user:
        list_anime = Anime.objects.order_by('name').filter(type='recommendations').values()
        url = "https://myanimelist.p.rapidapi.com/anime/top/bypopularity"

        headers = {
            "X-RapidAPI-Key": "0a0b72559emshc1ca09f720d7505p15e229jsnfcf4f42dc10a",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }
        data = None
        try:
            response = requests.get(url, headers=headers)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Handle the successful response
                data = response.json()
                # Process the data as needed
            else:
                # Handle other HTTP status codes (e.g., 404 Not Found, 500 Internal Server Error)
                messages.add_message(request, messages.ERROR,
                                     f"API request failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Handle general request exceptions (e.g., network issues)
            messages.add_message(request, messages.ERROR, "API request failed with exception:",
                                 e)
        except ratelimit.Ratelimited as e:
            messages.add_message(request, messages.ERROR, "Rate limit exceeded. Please try again later.",
                                 e)
            # Handle rate limit exceedance
            return HttpResponse("Rate limit exceeded. Please try again later.", status=429)
        except Exception as e:
            # Handle other unexpected exceptions
            messages.add_message(request, messages.ERROR, "An unexpected error occurred:",
                                 e)
        form = SearchForm()
        context = {
            'response': data,
            'list_anime': list_anime,
            'subcategory': 'recommendations',
            'form': form
        }
        return render(request, 'AnimePlayApp/category.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# category page for recent
@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def recent(request):
    user = request.user.is_authenticated
    if user:
        list_anime = Anime.objects.order_by('name').filter(type='recent').values()
        url = "https://myanimelist.p.rapidapi.com/anime/top/airing"

        headers = {
            "X-RapidAPI-Key": "0a0b72559emshc1ca09f720d7505p15e229jsnfcf4f42dc10a",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }
        data = None
        try:
            response = requests.get(url, headers=headers)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Handle the successful response
                data = response.json()
                # Process the data as needed
            else:
                # Handle other HTTP status codes (e.g., 404 Not Found, 500 Internal Server Error)
                messages.add_message(request, messages.ERROR,
                                     f"API request failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Handle general request exceptions (e.g., network issues)
            messages.add_message(request, messages.ERROR, "API request failed with exception:",
                                 e)
        except ratelimit.Ratelimited as e:
            messages.add_message(request, messages.ERROR, "Rate limit exceeded. Please try again later.",
                                 e)
            # Handle rate limit exceedance
            return HttpResponse("Rate limit exceeded. Please try again later.", status=429)
        except Exception as e:
            # Handle other unexpected exceptions
            messages.add_message(request, messages.ERROR, "An unexpected error occurred:",
                                 e)

        form = SearchForm()
        context = {
            'response': data,
            'list_anime': list_anime,
            'subcategory': 'recent',
            'form': form
        }
        return render(request, 'AnimePlayApp/category.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# sorting the list
def sorted_list(request, category_id,order_type):
    user = request.user.is_authenticated
    if user:
        if order_type == 'ASC':
            list_anime = Anime.objects.order_by('name').filter(type=category_id).values()
            form = SearchForm()
            context = {
                'list_anime': list_anime,
                'subcategory': category_id,
                'form': form
            }
            return render(request, 'AnimePlayApp/category.html', context)
        else:
            list_anime = Anime.objects.order_by('-name').filter(type=category_id).values()
            form = SearchForm()
            context = {
                'list_anime': list_anime,
                'subcategory': category_id,
                'form': form
            }
            return render(request, 'AnimePlayApp/category.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
#adding to watch list
def watchlist_add(request,anime_id):
    user = request.user.is_authenticated
    if user:
        list_anime = Anime.objects.order_by('name').filter(id=anime_id).values()
        for item in list_anime:
            name=item['name']
            aired=item['aired']
            type=item['type']
            studios=item['studios']
            description=item['description']
            img=item['img']
            video=item['video']
        # Check if the item already exists in that user watchlist
        if WatchList.objects.filter(user=request.user, name=name).exists():
            messages.add_message(request, messages.ERROR, "You already have "+name+" your watchlist")
            return redirect('/')
        # Get the user watchlist or create it if it doesn't exists
        un = request.user.username
        list_watchlist = WatchList(
            user=request.user,
            username=un,
            name=name,
            aired=aired,
            type=type,
            studios=studios,
            description=description,
            img=img,
            video=video
        )
        list_watchlist.save()

        verb = "Added to watchlist " + name
        actions = Action(
            user=request.user,
            verb=verb,
            target=list_watchlist
        )
        actions.save()

        # Add the item through the ManyToManyField (Watchlist => item)
        messages.add_message(request, messages.SUCCESS, "Successfully added "+name+" to your watchlist")
        return redirect('/watchlist')
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# listing all items in watchlist
def watchlist(request):
    user = request.user.is_authenticated
    if user:
        list_watchlist = WatchList.objects.order_by('name').filter(user=request.user).values()
        list_anime = Anime.objects.order_by('name').filter(type='recommendations').values()
        form = SearchForm()
        context = {
            'list_watchlist': list_watchlist,
            'list_anime': list_anime,
            'form':form
        }
        return render(request, 'AnimePlayApp/watchlist.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# search for any item in database
@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def search(request):
    user = request.user.is_authenticated
    if user:
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                search_query = form.cleaned_data['search_query']
                list_anime = Anime.objects.filter(name=search_query).values()
                url = "https://myanimelist.p.rapidapi.com/v2/anime/search"

                querystring = {"q": search_query, "n": "5", "score": "8"}

                headers = {
                    "X-RapidAPI-Key": "0a0b72559emshc1ca09f720d7505p15e229jsnfcf4f42dc10a",
                    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
                }
                data = None
                try:
                    response = requests.get(url, headers=headers, params=querystring)

                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        # Handle the successful response
                        data = response.json()
                        # Process the data as needed
                    else:
                        # Handle other HTTP status codes (e.g., 404 Not Found, 500 Internal Server Error)
                        messages.add_message(request, messages.ERROR,
                                     f"API request failed with status code: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    # Handle general request exceptions (e.g., network issues)
                    messages.add_message(request, messages.ERROR, "API request failed with exception:",
                                         e)
                except ratelimit.Ratelimited as e:
                    messages.add_message(request, messages.ERROR, "Rate limit exceeded. Please try again later.",
                                         e)
                    # Handle rate limit exceedance
                    return HttpResponse("Rate limit exceeded. Please try again later.", status=429)
                except Exception as e:
                    # Handle other unexpected exceptions
                    messages.add_message(request, messages.ERROR, "An unexpected error occurred:",
                                         e)

                form = SearchForm()
                context = {
                    'form': form,
                    'search_query':search_query,
                    'list_anime': list_anime,
                    'response': data
                }
                return render(request, 'AnimePlayApp/search.html',
                              context)
        else:
            form = SearchForm()
            return render(request, 'AnimePlayApp/search.html', {'form': form})
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# deleting a comment
def comment_del(request, search_query):
    user = request.user.is_authenticated
    if user and request.method == 'POST':
        delete_comment = Comment.objects.get(id=search_query)
        deleted_id = delete_comment.id
        deleted_anime_id = delete_comment.anime_id
        if(request.user.id == delete_comment.author_id or request.user.is_superuser):
            verb ="deleted a comment on "+ str(delete_comment.anime_id) + " by " + request.user.username
            actions = Action(
                user=request.user,
                verb=verb,
                target=delete_comment
            )
            actions.save()
            delete_comment.delete()
            messages.add_message(request, messages.WARNING, "Successfully Deleted Comment ",deleted_id)
            return redirect('/detail/'+str(deleted_anime_id))
        else:
            messages.add_message(request, messages.WARNING, "you dont have access to delete", deleted_id)
            return redirect('/detail/' + str(deleted_anime_id))

    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
#detail view for any anime page it includes comments also
@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def detail_id(request, search_query):
    user = request.user.is_authenticated
    if user:
        list_anime = Anime.objects.filter(id=search_query).values()
        allcomments = Comment.objects.filter(status=True, anime_id=search_query)
        page = request.GET.get('page', 1)
        #pageinator for comments
        paginator = Paginator(allcomments, 10)
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        user_comment = None
        edit_comment = None
        comment_anime = Anime.objects.get(id=search_query)
        method = request.POST.get('_method', '').lower()
        if request.method == 'POST':
            if method == 'post' :
                #for creating new comments
                comment_form = NewCommentForm(request.POST)
                if comment_form.is_valid() and request.user.username == request.POST.get('name'):
                    user_comment = comment_form.save(commit=False)
                    user_comment.anime = comment_anime
                    user_comment.author = request.user
                    user_comment.save()
                    name = request.POST.get('name')
                    verb = "Added a comment on " + str(user_comment.anime_id) + " by " + name
                    actions = Action(
                        user=request.user,
                        verb=verb,
                        target=user_comment
                    )
                    actions.save()
                    messages.add_message(request, messages.SUCCESS, "Successfully added Comment ")
                    return HttpResponseRedirect('/detail/' + search_query)
            elif method == 'delete':
                comment_form = NewCommentForm(request.POST)
                # for deleting a comment
            elif method == 'put' and request.user.username == request.POST.get('name'):
                #for editing an exisitng comment
                edit_comment_id = request.POST.get('parent')
                name = request.POST.get('name')
                email = request.POST.get('email')
                content = request.POST.get('content')
                edit_comment = get_object_or_404(Comment, id=edit_comment_id)
                edit_comment.name = name
                edit_comment.email = email
                edit_comment.content = content
                edit_comment.save()
                verb = "Edited a comment on " + str(edit_comment.anime_id) + " by " + name
                actions = Action(
                    user=request.user,
                    verb=verb,
                    target=edit_comment
                )
                actions.save()
                messages.add_message(request, messages.SUCCESS, "Successfully updated Comment ")
                return HttpResponseRedirect('/detail/' + search_query)
        # ajax request for getting the edited comment details
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
            edit_comment_id = request.GET.get('edit_comment_id')
            edit_comment = Comment.objects.get(id=edit_comment_id)

            # Serialize the comment data as needed
            serialized_data = {
                'content': edit_comment.content,
                'name': edit_comment.name,
                'email': edit_comment.email,
                'id': edit_comment.id
            }

            return JsonResponse(serialized_data)
        else:
            comment_form = NewCommentForm()
        form = SearchForm()
        url = "https://myanimelist.p.rapidapi.com/v2/anime/search"

        querystring = {"q": comment_anime.name, "n": "5", "score": "8"}

        headers = {
            "X-RapidAPI-Key": "0a0b72559emshc1ca09f720d7505p15e229jsnfcf4f42dc10a",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }
        data = None
        try:
            response = requests.get(url, headers=headers, params=querystring)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Handle the successful response
                data = response.json()
                # Process the data as needed
            else:
                # Handle other HTTP status codes (e.g., 404 Not Found, 500 Internal Server Error)
                messages.add_message(request, messages.ERROR,
                                     f"API request failed with status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Handle general request exceptions (e.g., network issues)
            messages.add_message(request, messages.ERROR, "API request failed with exception:",
                                 e)
        except ratelimit.Ratelimited as e:
            messages.add_message(request, messages.ERROR, "Rate limit exceeded. Please try again later.",
                                 e)
            # Handle rate limit exceedance
            return HttpResponse("Rate limit exceeded. Please try again later.", status=429)
        except Exception as e:
            # Handle other unexpected exceptions
            messages.add_message(request, messages.ERROR, "An unexpected error occurred:",
                                 e)
        context = {
            'list_anime': list_anime,
            'comments': user_comment,
            'comments': comments,
            'comment_form': comment_form,
            'allcomments': allcomments,
            'edit_comment': edit_comment,
            'form': form,
            'response': data
        }
        return render(request, 'AnimePlayApp/detail.html',
                      context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# adding new anime
def anime_add(request):
    user = request.user.is_authenticated
    if user:
        if request.method == 'POST':
            form = AddAnimeForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['Name']
                aired = form.cleaned_data['Aired']
                studios = form.cleaned_data['Studios']
                Description = form.cleaned_data['Description']
                Image = form.cleaned_data['Image']
                Video = form.cleaned_data['Video']
                Type = form.cleaned_data['Type']
                Add_anime = Anime(
                    name=name,
                    aired=aired,
                    studios=studios,
                    description=Description,
                    img=Image,
                    video=Video,
                    type=Type
                )
                Add_anime.save()

                verb = "added new animeDB " + str(Add_anime.id)
                actions = Action(
                    user=request.user,
                    verb=verb,
                    target=Add_anime
                )
                actions.save()
                messages.add_message(request, messages.SUCCESS, "Successfully added "+name+" to Anime Database")
                return redirect('/detail/'+str(Add_anime.id)+'/')
        else:
            form = AddAnimeForm()
            return render(request, 'AnimePlayApp/addanime.html', {})
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# editing an existing anime
def anime_edit(request, search_query):
    user = request.user.is_authenticated
    if user:
        if request.method == 'POST':
            form = AddAnimeForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['Name']
                aired = form.cleaned_data['Aired']
                studios = form.cleaned_data['Studios']
                Description = form.cleaned_data['Description']
                Image = form.cleaned_data['Image']
                Video = form.cleaned_data['Video']
                Type = form.cleaned_data['Type']
                edit_anime = Anime.objects.get(id=search_query)
                old_name = edit_anime.name
                edit_anime.name = name
                edit_anime.aired = aired
                edit_anime.studios = studios
                edit_anime.description = Description
                edit_anime.img = Image
                edit_anime.video = Video
                edit_anime.type = Type
                edit_anime.save()

                verb = "edited from animeDB " + str(edit_anime.id)
                actions = Action(
                    user=request.user,
                    verb=verb,
                    target=edit_anime
                )
                actions.save()
                messages.add_message(request, messages.INFO, "Successfully Edited "+old_name+" to Anime Database")
                return redirect('/detail/' + str(edit_anime.id) + '/')
        else:
            form = AddAnimeForm()
            list_anime= Anime.objects.filter(id=search_query).values()
            searchform = SearchForm()
            context = {
                'list_anime':list_anime,
                'form': form,
                'searchform':searchform
            }
            return render(request, 'AnimePlayApp/edit-anime.html', context)
    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})

# deleting an existing anime
def anime_delete(request, search_query):
    user = request.user.is_authenticated
    if user:
        if request.method == 'POST':
            form = DeleteAnimeForm(request.POST)
            if form.is_valid() and request.user.is_superuser:

                list_anime = Anime.objects.get(id=search_query)
                deleted_name = list_anime.name
                verb = "deleted from animeDB " + str(list_anime.id)
                actions = Action(
                    user=request.user,
                    verb=verb,
                    target=list_anime
                )
                actions.save()
                list_anime.delete()
                messages.add_message(request, messages.WARNING, "Successfully Deleted "+deleted_name+" from Anime Database")
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING,
                                     "you dont have access to delete anime only admin has access")
                return redirect('/')
        else:
            return redirect('/')

    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
# deleting an existing watchlist
def watchlist_delete(request, anime_id):
    user = request.user.is_authenticated
    if user:
        if request.method == 'POST':
            form = DeleteAnimeForm(request.POST)
            if form.is_valid():
                list_watchlist = WatchList.objects.get(id=anime_id)
                name = list_watchlist.name
                verb = "deleted from watchlist " + name
                actions = Action(
                    user=request.user,
                    verb=verb,
                    target=list_watchlist
                )
                actions.save()
                list_watchlist.delete()
                messages.add_message(request, messages.WARNING, "Removed  "+name+" from Watchlist")
                return redirect('/watchlist')
        else:
            return redirect('/tvseries')

    else:
        form = SearchForm()
        return render(request, 'AnimePlayAuthApp/login.html',{'form':form})
