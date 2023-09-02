import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {"name": "suraj"}) 

def add(request):
    v1 = request.POST["n1"]
    v2 = request.POST["n2"]
    res = int(v1)+ int(v2) 
    return render(request, 'result.html',{"result": res})
