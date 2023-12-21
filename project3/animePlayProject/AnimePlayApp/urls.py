from django.urls import path
from . import views
from AnimePlayAuthApp import views
from django.conf.urls import handler404
app_name = 'AnimePlayApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('tvseries/', views.series, name='series'),
    path('recommendations/', views.recom, name='recommendations'),
    path('recent/', views.recent, name='recent'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/<str:anime_id>', views.watchlist_add, name='watchlist_add'),
    path('watchlist/remove/<str:anime_id>', views.watchlist_delete, name='watchlist_delete'),
    path('search/', views.search, name='search'),
    path('detail/<str:search_query>/', views.detail_id, name='detail'),
    path('comment/<str:search_query>/deleted', views.comment_del, name='comment_del'),
    path('movies/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('tvseries/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('recommendations/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('recent/detail/<str:search_query>/', views.detail_id, name='detail'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/profile/<str:username>', views.profile_view, name='profile'),
    path('auth/profile/<str:username>/edit', views.profile_edit, name='profile_edit'),
    path('auth/profile/<str:username>/delete', views.profile_del, name='profile_del'),
    path('addanime/', views.anime_add, name='anime_add'),
    path('editanime/<str:search_query>/', views.anime_edit, name='anime_edit'),
    path('deleteanime/<str:search_query>/', views.anime_delete, name='anime_delete'),
    path('sorted_list/<str:category_id>/<str:order_type>', views.sorted_list, name='sorted_list'),

]