from dataclasses import field
from pyexpat import model
from django.forms import ModelForm, PasswordInput
# from matplotlib.pyplot import cla
from .models import Room
from django import forms

from django.contrib.auth.models import User

from .models import UserProfileInfo

from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'



class UserGet(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=PasswordInput)

    class Meta():
        model  = User

        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():

        model = UserProfileInfo

        fields = ('portfolio_site', 'profile_pic')
