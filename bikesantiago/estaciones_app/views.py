import requests
from django.shortcuts import render
from .models import Estacion

def estaciones_view(request):
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    estaciones = response.json()['network']['stations']
    for estacion in estaciones:
        Estacion.objects.update_or_create(
            id_estacion=estacion['id'],
            defaults={
                'nombre':estacion['name'],
                'latitud':estacion['latitude'],
                'longitud':estacion['longitude'],
                'espacios_vacios':estacion['empty_slots']
            }
        )
    return render(request, 'estaciones_app/estaciones.html', {'estaciones': estaciones})