"""
URL configuration for imagineApps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from logistics import views
from logistics.Paquetes import views as viewsPaquetes

urlpatterns = [
    path('', viewsPaquetes.listar_paquetes,name='home'),
    path('admin/', admin.site.urls),
    path('asignar_paquete_transportista/', views.asignar_paquete_transportista, name='asignar_paquete_transportista'),
    path('listar_paquete/', views.listar_paquete, name='listar_paquete'),
    path('obtener_paquetes/<int:id_usuario>/', views.obtener_paquetes, name='obtener_paquetes'),
    path('modal_eliminar/<int:id_paquete>/', viewsPaquetes.modal_eliminar, name='modal_eliminar'),
    path('',include('logistics.urls'))
    
]
