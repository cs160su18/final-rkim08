from django.views import generic
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
import json
from las.models import *

# Create your views here.
def index(request):
  return render(request, 'las/index.html')
def guide(request):
  return render(request, 'las/guide.html')
def search(request):
  return render(request, 'las/search.html') 
def collections(request):
  return render(request, 'las/collections.html')
def login(request):
  return render(request, 'las/login.html')
def post(request):
  return render(request, 'las/post.html')


# class searchView(generic.ListView):
#   template_name='las/search.html
  
#   def get_queryset(self):
#     return Users.objects.all()
  

# class DetailView(generic.DetailView)L
  
