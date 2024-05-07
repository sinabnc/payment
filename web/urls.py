from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("",views.index,name='index'),
    path('login',views.login1,name="login"),
    path('singup',views.singup,name="singup"),
    path('logout',views.logout1,name="logout"),
    path('price',views.price,name="price"),
    path('deva',views.deva,name="deva"),
    path('card',views.card,name="card"),
    path('fal',views.fal,name="fal"),



    path('accounts/', include('allauth.urls')),
   





]
