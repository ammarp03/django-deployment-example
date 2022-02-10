import email
from django import forms
from django.forms import ModelForm
from .models import User2

class FormNAme(forms.Form):

    name = forms.CharField()

    email = forms.EmailField()

    text = forms.CharField(widget=forms.Textarea)

class User2Form(ModelForm):
    class Meta:
        model = User2
        fields = '__all__'