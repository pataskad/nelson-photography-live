from django import forms


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(required=True, widget=forms.Textarea, max_length=1000)