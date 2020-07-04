from django.contrib import admin
from .models import Marca, Tipo, Modelo, Auto, Marca_Tipo
# Register your models here.

admin.site.register(Marca)
admin.site.register(Tipo)
admin.site.register(Modelo)
admin.site.register(Auto)
admin.site.register(Marca_Tipo)