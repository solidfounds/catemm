from django.db import models
# Create your models here.




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
    operador = models.ManyToManyField('users.User')
    
    class Meta:
        verbose_name_plural = 'Primer Registro'
    def __str__(self):
        return self.nombre



class SegundoRegistro(models.Model):
    cliente = models.ForeignKey(PrimerRegistro)
    fecha = models.DateField(auto_now_add=True)
    caratula =  models.CharField(max_length=50)
    tarjeta_de_mejoravit = models.FileField(upload_to='media/targeta_infonavit')
    numero_tarjeta = models.SmallIntegerField()
    tarjeta_entregada = models.BooleanField()
    tarjeta_activa = models.BooleanField()
    tarjeta_con_fondos = models.BooleanField()
    credito = models.DecimalField(max_digits=7,decimal_places=2, blank=True, null=True )
    operador = models.ForeignKey('users.User')



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



class Productos (models.Model):
    name = models.CharField(max_length=100)
    price = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Venta(models.Model):
    cliente = models.ForeignKey(PrimerRegistro)
    detalle_venta = models.ManyToManyField(Productos)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(blank=True,decimal_places=2,default=0,editable=True,max_digits=9,null=True,verbose_name='Total')
    def __str__(self):
        return self.cliente.nombre

class DetalleVenta_(models.Model):
    producto = models.ForeignKey(Productos)
    venta = models.ForeignKey(Venta)
    # precio_venta = models.DecimalField(blank=True,decimal_places=2,default=0,editable=True,max_digits=9,null=True,verbose_name='Precio Venta')
    cantidad = models.PositiveSmallIntegerField(blank=True,default=0,null=True)
    def __str__(self):
        return "%s = %s" % (self.producto.nombre, self.producto.precio)