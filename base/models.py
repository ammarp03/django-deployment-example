# from operator import mod
# from pyexpat import model
# import re
# from turtle import update
# from unicodedata import name
# from operator import mod
from distutils.command.upload import upload
import email
from operator import mod
from pydoc_data.topics import topics
from statistics import mode
# from sys import last_type
from django.db import models
from django.contrib.auth.models import User

# Create your models here.












class Topic(models.Model):
    name  = models.CharField(max_length=200)


    def __str__(self):
       return self.name






class Room(models.Model):

    host = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    topic = models.ForeignKey(Topic , on_delete=models.SET_NULL , null=True)
    # date = models.ForeignKey(AccessRecord , on_delete=models.SET_NULL , null=True)


    

    
    name = models.CharField(max_length=200)
    discription  = models.TextField(null=True , blank= True , max_length=1000 )


    # participent  = 

    updated = models.DateTimeField(auto_now=True)
 
    created  = models.DateTimeField(auto_now_add=True)

    class Meta:
    
    # updated wil creat most latest data at the top by using -
        ordering = ['-updated' , '-created']
    


    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    room = models.ForeignKey(Room , on_delete=models.CASCADE)
    
    body = models.TextField()

    updated = models.DateTimeField(auto_now=True)

    created  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[0:50]




class Topic2(models.Model):
    name  = models.CharField(max_length=200)
    


    def __str__(self):
       return self.name



class Webpage(models.Model):
    





    
    host = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)

    topic = models.ForeignKey(Topic2 , on_delete=models.SET_NULL , null=True)
    name = models.CharField(max_length=200 , unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return str(self.name)



class AccessRecord(models.Model):
    # name = models.ForeignKey(Message, on_delete=models.CASCADE)
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE, null=True)
    date = models.DateField()

    def __str__(self):
        return str(self.date)



class User2(models.Model):
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    
    
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    portfolio_site = models.URLField(blank=True)


    profile_pic = models.ImageField(upload_to = 'images', blank = True)

    def __str__(self):

        return self.user.username







    # def __str__(self):
    #     return self.email


    


    # class Webpage(models.Model):
    # topic = models.Fo`reignKey(Message, on_delete=models.CASCADE)
    # name = models.CharField(max_length=264, unique=True)
#     url = models.URLField(unique=True)

#     def __str__(self):
#         return self.name

# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
#     date = models.DateField()

#     def __str__(self):
#         return str(self.date)




    
    
    # SET_NULL
