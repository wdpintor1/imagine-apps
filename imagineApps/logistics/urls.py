from django.urls import path
from logistics.Paquetes import views

urlpatterns = [
    path('paquetes/', views.listar_paquetes, name='listar_paquetes'),  
    path('crear_actualizar_paquete/', views.crear_actualizar_paquete, name='crear_paquete'),
    path('crear_actualizar_paquete/<int:idPaquete>/', views.crear_actualizar_paquete, name='actualizar_paquete'),
    path('eliminar_paquete/<int:id_paquete>/', views.eliminar_paquete, name='eliminar_paquete'),
    path('editar_paquete/<int:id_paquete>/', views.crear_actualizar_paquete, name='editar_paquete')
    
]