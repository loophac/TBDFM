from django.http import HttpResponse
import requests
from django.shortcuts import render

def home(request):
  home = 'TBDFM/home.html'
  return render(request, home)