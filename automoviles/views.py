from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView 
from .models import Marca, Tipo
from .forms import MarcaForm, TipoForm
from django.urls import reverse_lazy
# Create your views here.

class Home(TemplateView):
    template_name = 'automovil/index.html'

class listarMarcas(ListView):
    model = Marca
    template_name = 'automovil/marca/listar_marcas.html'
    queryset = Marca.objects.all()
    context_object_name = 'marcas'

class CrearMarca(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'automovil/marca/crear_marcas.html'
    success_url = reverse_lazy('listar.marcas')



# class ListarAutos(ListView):
#     model = Author
#     template_name = 'automovil/auto/lista_autos.html'
#     queryset = Author.objects.all()
#     context_object_name = 'authors'

