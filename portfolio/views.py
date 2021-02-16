from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        
        form=contactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            send_mail( name, message, sender, ['nelsonj@pixbyjade.com'])
            messages.success(request, 'Thank you! I will be reaching out ASAP')
        return HttpResponseRedirect('/thanks')
    else:
        form = contactForm()
    return render(request, 'index.html', {'form': form})


def thanks(request):
    form = contactForm()
    messages.success(request, 'Thank you! I will be reaching out ASAP')
    return render(request, 'index.html', {'form': form})

