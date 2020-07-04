from django.db import models

# Create your models here.

class Marca(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_marca = models.CharField(max_length = 50, blank = False, null = False)

    def __str__(self):
        return self.nombre_marca
    
    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['nombre_marca']

class Tipo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_tipo = models.CharField(max_length = 50, blank = False, null = False)
    

    def __str__(self):
        return self.nombre_tipo

    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        ordering = ['nombre_tipo']

class Marca_Tipo(models.Model):
    id = models.AutoField(primary_key = True)
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete= models.CASCADE)
    

    def __str__(self):
        return str(self.marca.nombre_marca) + ' - ' + str(self.tipo.nombre_tipo)

class Modelo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_modelo = models.CharField(max_length = 50, blank = False, null = False)
    marca_tipo = models.ForeignKey(Marca_Tipo, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre_modelo

    class Meta:
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'
        ordering = ['nombre_modelo']

class Auto(models.Model):
    id = models.AutoField(primary_key = True)
    marca_tipo = models.ForeignKey(Marca_Tipo, on_delete = models.CASCADE , null = True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete = models.CASCADE)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to= 'pictures/autos')
    caracteristicas = models.FileField(upload_to = 'files/autos')

