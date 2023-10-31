from django.urls import path
from . import views
from AnimePlayAuthApp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('tvseries/', views.series, name='series'),
    path('recommendations/', views.recom, name='recommendations'),
    path('recent/', views.recent, name='recent'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('search/', views.search, name='search'),
    path('detail/<str:search_query>/', views.detail_id, name='detail'),
    path('movies/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('tvseries/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('recommendations/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('recent/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
]