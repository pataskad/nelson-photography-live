from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect

def index(request):
   
    return render(request, 'index.html')


