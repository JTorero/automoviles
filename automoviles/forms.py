from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Auto, Marca, Tipo

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre_marca']
        labels = {
                'nombre_marca' :'nombre_marca '
            }
        widgets = {
            'nombre_marca': TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Ingrese el nombre del marca',
                    'id' : 'nombre_marca'
                }
            )
        }

class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre_tipo']
        labels = {
            "nombre_tipo" :'nombre_tipo '
        }
        widgets = {
            'nombre_tipo': TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Ingrese el nombre del tipo',
                    'id' : 'nombre_tipo'
                }
            )
        }
