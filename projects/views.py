from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    return render(request,'index.html')