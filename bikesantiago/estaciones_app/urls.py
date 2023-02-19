from django.urls import path
from .views import estaciones_view

urlpatterns = [
    path('', estaciones_view, name='estaciones'),
]
