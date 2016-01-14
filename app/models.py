from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sucursales(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    telefono = models.SmallIntegerField()
    renta = models.DecimalField(max_digits=7, decimal_places=2)
    luz = models.DecimalField(max_digits=7, decimal_places=2)
    agua = models.DecimalField(max_digits=7, decimal_places=2)
    varios = models.DecimalField(max_digits=7, decimal_places=2)

    
    class Meta:
        verbose_name_plural = 'Sucursales'
    def __str__(self):
        return self.nombre



PORCENTAJE_GANANCIA_CHOICES = (
    ('3', '3%'),
    ('4', '4%'),
    ('5', '5%'),
    ('6', '6%'),
)



PERSONAL_CHOICES = (
    ('1', 'Asesor'),
    ('2', 'Asistente'),
)
class Personal(models.Model):
    user = models.OneToOneField(User, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    porcentaje_ganancia = models.CharField(max_length=1, choices=PORCENTAJE_GANANCIA_CHOICES)
    sucursal = models.OneToOneField(Sucursales)
    clave = models.CharField(max_length =10)
    num_de_cuenta = models.CharField(max_length=20)
    banco = models.CharField(max_length=50)
    telefono_casa = models.SmallIntegerField()
    telefono_celular= models.SmallIntegerField()
    email = models.EmailField()
    ife = models.FileField(upload_to='media/empleados/ifes')
    tipo_personal = models.CharField(max_length=1, choices=PERSONAL_CHOICES)
    
    class Meta:
        verbose_name_plural = 'Personal'
    def __str__(self):
        return self.nombre

#lo hace el asesor asesoria para obtene el plastico
class PrimerRegistro(models.Model):
    nombre = models.CharField(max_length=55)
    apellidos = models.CharField(max_length=80)
    direccion = models.TextField()
    nsn = models.CharField(max_length=15)
    telefono= models.SmallIntegerField()
    empresa = models.CharField(max_length=254)
    registro_patronal = models.CharField(max_length=15)
    comision = models.DecimalField(max_digits=7, decimal_places=2)
    ife = models.FileField(upload_to='media/ifes')

    email = models.EmailField()
    numero_de_cuenta = models.CharField(max_length=16)
    banco = models.CharField(max_length=15)
    operador = models.OneToOneField(Personal)
    
    class Meta:
        verbose_name_plural = 'Primer Registro'
    def __str__(self):
        return self.nombre
"""
class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Articulos'
        
    def __str__(self):
        return self.nombre

COMPRAS_CHOICES = (
    ('1', 'Compra 1'),
    ('2', 'Compra 2'),
)

class Compras(models.Model):
    tipo_compra = models.CharField(max_length=1, choices=COMPRAS_CHOICES)
    articulos = models.ForeignKey(Articulos)
    cantidad = models.SmallIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_unitario(self):
        return self.articulos.precio

    def totala(self):
        return self.cantidad * self.articulos.precio
    
    class Meta:
        verbose_name_plural =    'Compras'       
    
    def __str__(self):
        return  u"%s %s " % (self.tipo_compra, self.total)
"""

#asistente        
class SegundoRegistro(models.Model):
    cliente = models.ForeignKey(PrimerRegistro)
    fecha = models.DateField(auto_now_add=True)
    caratula =  models.CharField(max_length=50)
    tarjeda_de_mejoravit = models.FileField(upload_to='media/targeta_infonavit')



    class Meta:
        verbose_name_plural = 'Segundo Registro'
        
    def __str__(self):
        return self.cliente.nombre


#en teoria este es el segundo
class TercerRegistro(models.Model):
    cliente = models.ForeignKey(PrimerRegistro)
    compra = models.TextField()
    importe_total = models.DecimalField(max_digits=10, decimal_places=2)
    efectivo = models.DecimalField(max_digits=10, decimal_places=2)
    comision =  models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    numero_credito = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = 'Tercer Registro'
    def __str__(self):
        return self.cliente
