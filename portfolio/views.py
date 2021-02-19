from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail



def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def thanks(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        return render(request, 'index.html', {'name': name})
    else:
        return render(request, 'index.html')

