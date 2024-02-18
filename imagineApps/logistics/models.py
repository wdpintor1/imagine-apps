from django.db import models
from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    # Establece manualmente el valor predeterminado para fecha_creacion
    fecha_creacion = models.DateTimeField(default=timezone.now, blank=True)    
    # Usa auto_now para fecha_actualizacion
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    def __int__(self):
        return self.idCliente

class Transportista(models.Model):
    idTransportista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_vehiculo = models.CharField(max_length=50)
    numero_contacto = models.CharField(max_length=20)
    disponible=models.CharField(max_length=1)
    # Establece manualmente el valor predeterminado para fecha_creacion
    fecha_creacion = models.DateTimeField(default=timezone.now, blank=True)    
    # Usa auto_now para fecha_actualizacion
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    idPaquete = models.AutoField(primary_key=True)
    peso = models.IntegerField()
    dimensiones = models.CharField(max_length=50)
    direccion_origen = models.CharField(max_length=255)
    direccion_destino = models.CharField(max_length=255)
    estado_entrega = models.CharField(max_length=20)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idTransportista = models.ForeignKey(Transportista, on_delete=models.CASCADE,null=True)
    # Establece manualmente el valor predeterminado para fecha_creacion
    fecha_creacion = models.DateTimeField(default=timezone.now, blank=True)    
    # Usa auto_now para fecha_actualizacion
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.idPaquete)  

class TipoUsuario(models.Model):
    idTipoUsuario = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion