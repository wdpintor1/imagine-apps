from django.shortcuts import render
from django.http import JsonResponse
from .models import Paquete, Transportista
import json
from django.views.decorators.csrf import csrf_exempt

def home(request):    
    return render(request, 'home.html')

@csrf_exempt
def asignar_paquete_transportista(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_paquete = data.get('id_paquete')
            id_transportista = data.get('id_transportista')
            estado=data.get('estado')
            if not (isinstance(id_paquete, int) and isinstance(id_transportista, int)):
                return JsonResponse({'error': 'Los IDs deben ser enteros'}, status=400)

            paquete = Paquete.objects.get(idPaquete=id_paquete)
            transportista = Transportista.objects.get(idTransportista=id_transportista)            
            
            paquete.idTransportista = transportista
            paquete.estado_entrega=estado
            paquete.save()            
            return JsonResponse({'message': 'Paquete asignado correctamente'}, status=200)
        except (Paquete.DoesNotExist, Transportista.DoesNotExist):
            return JsonResponse({'error': 'Paquete o transportista no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)