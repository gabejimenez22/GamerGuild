from django.urls import path
from . import views


urlpatterns = [

    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginpage, name="login"),

    path('register/', views.registerpage, name="register"),

    path('',views.home,name= "home"),
    path('room/<str:pk>/',views.room,name= "room"),
    path('profile/<str:pk>/',views.userprofile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteroom, name="delete-room"),
    path('delete-mesage/<str:pk>/', views.deletemessage, name="delete-message"),
]