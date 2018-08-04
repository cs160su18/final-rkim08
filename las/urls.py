from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guide', views.guide, name='guide'),
    path('search', views.search, name='search'),
    path('collection', views.collections, name='collections'),
    path('login', views.login, name='login'),
]