from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guide', views.guide, name='guide'),
    path('search', views.search, name='search'),
    path('collection', views.collections, name='collections'),
    path('login', views.login, name='login'),
    path('collection/post', views.post, name='post'),
    
    url(r'^login/$', auth_views.login, {'template_name':'las/login.html'}, name='login'),
#     url(r'^logout/$', auth_views.logout, name='logout'),
#     url(r'^admin/', admin.site.urls),
]