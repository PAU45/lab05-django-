from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"