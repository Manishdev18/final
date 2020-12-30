from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("travel",views.travel,name='travel'),
    path("food",views.food,name='food'),
    path('register',views.register,name='register'),

   
]
