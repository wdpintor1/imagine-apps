from django.contrib import admin
from django.urls import path,include
from logistics import views

urlpatterns = [  
     path('', include('logistics.Paquetes.urls')),
    
]
