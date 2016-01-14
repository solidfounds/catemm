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
    operador = models.OneToOneField('users.User')
    
    class Meta:
        verbose_name_plural = 'Primer Registro'
    def __str__(self):
        return self.nombre



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
