from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):

    return render(request,"templates/mainsite/index.html)