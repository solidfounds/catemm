from django.contrib import admin
from .models import User, Sucursal

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password', 'email', 'first_name', 'last_name', 'tipo', 'porcentaje_ganancia', 'sucursal', 'clave', 'num_de_cuenta','banco')

@admin.register(Sucursal)
class AdminSucursal(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'estado', 'telefono', 'renta', 'luz', 'agua', 'varios')