from django.shortcuts import render, redirect, get_object_or_404
from ..models import Paquete, Cliente
from django.core.paginator import Paginator, EmptyPage
from .forms import PaqueteForm
from django.contrib import messages

def listar_paquetes(request):
    # Filtra los canales por el usuario que ha iniciado sesión y los ordena por fecha de actualización descendente
    paquetes = Paquete.objects.all().order_by('fecha_creacion')
    # Configura la paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(paquetes, 4)  # Muestra 5 canales por página   
    try:
        paquetes = paginator.page(page)
    except EmptyPage:
        paquetes = paginator.page(paginator.num_pages)
    
    return render(request, 'paquetes.html', {'paquetes': paquetes})

def crear_actualizar_paquete(request, idPaquete=None):
    # Si se proporciona un idPaquete, se está actualizando un paquete existente
    if idPaquete:
        paquete = get_object_or_404(Paquete, idPaquete=idPaquete)
    else:
        paquete = None

    if request.method == 'POST':
        form = PaqueteForm(request.POST, instance=paquete)
        if form.is_valid():
            paquete = form.save(commit=False)  # Guarda el formulario pero no lo añade a la base de datos todavía
            paquete.estado_entrega = 'Enviado'
            print(form.cleaned_data['cliente'])
            # Obtener el cliente seleccionado en el formulario
            cliente_id = form.cleaned_data['cliente']
            cliente = Cliente.objects.get(idCliente=cliente_id)
            # Asignar la instancia del cliente al paquete
            paquete.idCliente = cliente
            paquete.save()
            messages.success(request, '¡Operación exitosa!')
            return redirect('/paquetes/')  # Redirige a la página principal después de guardar el paquete
    else:
        # Si no es una solicitud POST, inicializa el formulario con el paquete (si existe) y establece el estado de entrega predeterminado si se crea un nuevo paquete
        initial_data = {'estado_entrega': 'Enviado'} if not paquete else None
        form = PaqueteForm(instance=paquete, initial=initial_data)
    
    return render(request, 'crear_actualizar_paquete.html', {'form': form})

def modal_eliminar(request,id_paquete=None):
    print(id_paquete)
    return render(request, 'modal.html',{'id_paquete':id_paquete})

def eliminar_paquete(request, id_paquete):
    # Obtener el paquete a eliminar
    paquete = get_object_or_404(Paquete, idPaquete=id_paquete)
    # Eliminar el paquete
    paquete.delete()
    messages.success(request, '¡Registro eliminado correctamente!')
    # Redirigir a la página de paquetes
    return redirect('/paquetes')