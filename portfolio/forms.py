from django import forms



#this contact form is not being used for anything, keeping it here for the time being just in case as of 02/19/21
class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(required=True, widget=forms.Textarea, max_length=1000)

