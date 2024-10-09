# web/urls.py
from django.urls import path
from .views import index  # Cambia 'home' por 'index'

urlpatterns = [
    path('', index, name='index'),  # Asegúrate de que esta línea esté presente
]
