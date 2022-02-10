from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home , name="home"),
    path('room/<str:pk>/',views.room, name="room"),
    path('createRoom/',views.createRoom, name="create-room"),
    path('updateroom/<str:pk>/',views.updateRoom, name="update-room"),

    path('deleteroom/<str:pk>/',views.deleteRoom, name="delete-room"),


    path('user_email/',views.user_email, name="user_email"),
    # path('products/', views.products),
    # path('customer/', views.customer),
    # path('index/' , views.index),
    path('furm/', views.form_name_view, name="form_name_view"),


    path('filter/', views.filter, name="filter"),

    path('index/', views.index, name = "index"),

    path('register/', views.registration, name='register'),

    path('logout/', views.user_logout, name="logout"),
    path('special/' , views.special, name='special'),
    path('user_login', views.user_login, name= "user_login"),

    path('login/', views.loginPage, name = "login" )


]

