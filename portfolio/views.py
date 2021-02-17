from django.shortcuts import render, redirect
from .forms import contactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError



def index(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            subject = "Contact Request"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'pixbyjadecontact@gmail.com', ['nelsonj@pixbyjade.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks')

    form = contactForm()
    return render(request, 'index.html', {'form': form})


def thanks(request):
    form = contactForm()
    messages.success(request, 'Thank you! I will be reaching out ASAP')
    return render(request, 'index.html', {'form': form})

