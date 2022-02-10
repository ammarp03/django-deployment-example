# from multiprocessing import context
# from cProfile import Profile
# from multiprocessing import context
# import re
# import re
# from cProfile import Profile
from email import message
# from tkinter.messagebox import RETRY
from urllib.request import Request
from django import forms
from django.contrib import messages
from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Q

from .forms import UserGet

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
# from matplotlib.style import use
# from matplotlib.style import use
# from responses import registered
# from matplotlib.style import use

from .models import Room, Topic,Topic2, User2,Webpage,Message,AccessRecord,UserProfileInfo
from .forms import RoomForm, UserForm, UserProfileInfoForm
from .furm import FormNAme
from base import furm
from .furm import User2Form


# Create your views here.
# from  studybud import 



# Create your views here.
# def home(request):
#     return HttpResponse("Home Page")

# def products(request):
#     return HttpResponse("product")

# def customer(request):
#     return HttpResponse("customer")

# rooms = [
#     {'id' : 1, 'name' : 'Lets Learn Python'},
#     {'id' : 2, 'name' : 'Design with me '},
#     {'id' : 3, 'name' : 'Front end developer'},

# ]
def loginPage(request):
    

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # if user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User name or Password does not exit')
    
    context = {}

    return render(request , 'accounts/login_register.html', context)

def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''


    rooms = Room.objects.filter(
    Q(topic__name__icontains=q) |
    Q(name__icontains=q) |
    Q(discription__icontains=q)
    )


    topics = Topic.objects.all()

    room_count = rooms.count()
    context = {'rooms' : rooms , 'topics': topics, 'room_count':room_count}
    return render(request , 'accounts/dashboard.html' , context)

def room(request , pk ):
    room  = Room.objects.get(id=pk)

    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room' : room}
    return render (request , 'accounts/room.html' , context)
    

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}


    return render (request , 'accounts/room_form.html' , context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form =RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home') 

    context  = {'form': form}


    return render(request, 'accounts/room_form.html', context)

def deleteRoom(request, pk):
    room  = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}

    return render(request, 'accounts/delete.html', context)








def user_email(request):

    user_list = User2.objects.order_by('first_name')
    user_dict = {'users1': user_list}


    return render(request , 'accounts/home.html', context=user_dict)


def form_name_view(request):
    form = User2Form()
    if request.method == 'POST':
        # print(request.POST)
        form = User2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}


    return render (request , 'accounts/furm.html' , context=context)






def filter(request):
    context_dict = { 'text' : 'hello world' , 'number': 100 }

    return render(request , 'accounts/filter.html' , context=context_dict)


def index(request):
    return redirect('home')

    return render(request , 'accounts/index.html')


@login_required
def special(request):

    return HttpResponse('you are Log in Nice!')



@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('home'))

def registration(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data= request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True   
        else:
             
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()

        profile_form = UserProfileInfoForm()

                



        

    return render(request, 'accounts/registration.html',
                                    {'user_form': user_form,
                                    'profile_form': profile_form,
                                    'registered' : registered})



def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse('ACCOUNTS NOT ACTIVE')

        else:
            print("Some tried to log and failed")

            print("Username: {} and Password {}".format(username,password))

            return HttpResponse("invalid Log in detail Supplied")
    else:
        return render(request , 'accounts/login.html', {})




# def loginPage(request):


#     if request.method == 'POST':

#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'User does not exist')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'User name or Password does not exit')
    
#     context = {}

#     return render(request , 'accounts/login_register.html', context)




    # form = furm.FormNAme()



    # # constext = {'form': form}
    # if request.method == 'POST':
    #     form = furm.FormNAme(request.POST)
    #     if form.is_valid:
    #         print("Succes post")
    #         print("Name:" +form.cleaned_data['name'])
    #         print("Email:" +form.cleaned_data['email'])
    #         print("Text:" +form.cleaned_data['text'])




    # form.cleaned_data['name']
    # return render(request , 'accounts/furm.html', {'form': form})
 


 

# def customer(request):
#     return render(request,"accounts/customer.html")

# def index(request):
#     my_dict  = {'insert_me' : "Hello I am from view.py"}

#     return render(request , 'accounts/index.html' , context=my_dict)


