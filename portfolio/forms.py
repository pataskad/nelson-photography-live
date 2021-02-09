from django import forms

class contactForm(forms.Form):
    email=forms.EmailField(required=True)
    name=forms.CharField(max_length=100, required=True)
    message=forms.CharField(widget=forms.Textarea,required=True)