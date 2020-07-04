from django.urls import path, include
from .views import Home, listarMarcas, CrearMarca
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('listar_marcas', listarMarcas.as_view(), name='listar.marcas'),
    path('crear_marca', CrearMarca.as_view(), name='crear.marca')
]