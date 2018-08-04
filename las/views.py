from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.serializers import serialize
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
