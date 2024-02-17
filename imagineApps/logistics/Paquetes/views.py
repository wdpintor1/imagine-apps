from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from ..models import Paquete
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import CreateView
from ..forms import PaqueteForm
from django.contrib import messages
from django.views.generic import View

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
            # Antes de guardar el formulario, establece el estado de entrega como 'pendiente' si no se proporcionó
            if not paquete:
                paquete = form.save(commit=False)  # Guarda el formulario pero no lo añade a la base de datos todavía
                paquete.estado_entrega = 'pendiente'
                paquete.save()  # Ahora guarda el paquete con el estado de entrega establecido
            else:
                form.save()
                messages.success(request, '¡El canal y los campos fueron modificados con éxito!', extra_tags='claseMsj')
            return redirect('/paquetes/')  # Redirige a la página principal después de guardar el paquete
    else:
        # Si no es una solicitud POST, inicializa el formulario con el paquete (si existe) y establece el estado de entrega predeterminado si se crea un nuevo paquete
        initial_data = {'estado_entrega': 'pendiente'} if not paquete else None
        form = PaqueteForm(instance=paquete, initial=initial_data)

    return render(request, 'crear_actualizar_paquete.html', {'form': form})

def eliminar_paquete(request, id_paquete):
    # Obtener el paquete a eliminar
    paquete = get_object_or_404(Paquete, idPaquete=id_paquete)
    # Eliminar el paquete
    paquete.delete()
    # Redirigir a la página de paquetes
    return redirect('/paquetes')