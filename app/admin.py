from django.contrib import admin
from .models import  PrimerRegistro,SegundoRegistro, TercerRegistro
from users.models import Sucursal
# Register your models here.
"""
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
"""





# @admin.register(Personal)
# class AsesorAdmin(admin.ModelAdmin):
#     #list_display = ('clave','nombre', 'apellidos', 'porcentaje_ganancia', 'sucursal', 'num_de_cuenta', 'banco', 'telefono_casa', 'email', 'ife')
#     #list_filter = ('sucursal__nombre','porcentaje_ganancia')
#     pass


@admin.register(PrimerRegistro)
class PrimerRegistroAdmin(admin.ModelAdmin):
    #list_display = ('nombre', 'apellidos', 'direccion','nsn','telefono_casa','telefono_celular', 'empresa','registro_patronal','facturacion','comision','acta_de_nacimiento','ife','email','operador_que_lo_registro')
    #list_filter = ('operador_que_lo_registro__nombre','fecha')
    pass


@admin.register(SegundoRegistro)
class SegundoRegistroAdmin(admin.ModelAdmin):
    #list_display = ('cliente', 'fecha', 'caratula','tarjeda_de_mejoravit', 'numero_cuenta', 'banco')
    pass

"""
@admin.register(Articulos)
class ArticulosAdmin(admin.ModelAdmin):
    #list_display = ('nombre','precio',)
    pass


@admin.register(Compras)
class ComprasAdmin(admin.ModelAdmin):
    #list_display=('articulos','precio_unitario' ,'cantidad', 'tipo_compra', 'totala')
    #list_filter = ('tipo_compra',)
    pass
"""
@admin.register(TercerRegistro)
class TercerRegistroAdmin(admin.ModelAdmin):
    #list_display = ('cliente', 'compra', 'importe_total', 'efectivo', 'comision', 'fecha')
    #raw_id_fields = ('compra',)

    pass