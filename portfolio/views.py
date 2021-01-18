from django.shortcuts import render, redirect
from django.conf import settings

from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')