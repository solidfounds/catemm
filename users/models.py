

from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Sucursal(models.Model):
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



class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('el email deve de ser obligatorio')
        user = self.model(username = username, email=email, is_active= True, is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

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


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    password = make_password(password='testing',
                                  salt=None,
                                  hasher='unsalted_md5')
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=PERSONAL_CHOICES)
    porcentaje_ganancia = models.CharField(max_length=1, choices=PORCENTAJE_GANANCIA_CHOICES)
    sucursal = models.ForeignKey(Sucursal, blank=True, null=True)
    clave = models.CharField(max_length =10)
    num_de_cuenta = models.CharField(max_length=20)
    banco = models.CharField(max_length=50)


    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username
