from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from portfolio.forms import contactForm



def index(request):
    if request.method == 'GET':
        form_class = contactForm
        form = form_class(None)
        context = {
                'form': form,
            }
        return render(request, 'index.html', context)
    if request.method == 'POST':
        
        form=contactForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            name=form.cleaned_data['name']
            message=form.cleaned_data['message']
    
            send_mail(name, message, email, ['nelsonj@pixbyjade.com'], fail_silently=False)

        else:
            form = contactForm()
            context = {
                'form': form,
            }
    return redirect('/')

