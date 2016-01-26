from django.contrib import admin
from .models import  PrimerRegistro,SegundoRegistro, Productos, Order, ProductOrder
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


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    pass

@admin.register(PrimerRegistro)
class PrimerRegistroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'direccion','nsn','telefono','empresa','registro_patronal','comision','ife','email','numero_de_cuenta','banco')
    #list_filter = ('operador_que_lo_registro__nombre','fecha')
    pass


@admin.register(SegundoRegistro)
class SegundoRegistroAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'caratula','tarjeta_de_mejoravit', 'numero_tarjeta','tarjeta_entregada','tarjeta_activa','tarjeta_con_fondos','credito', 'operador')
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
"""
@admin.register(TercerRegistro)
class TercerRegistroAdmin(admin.ModelAdmin):
    #list_display = ('cliente', 'compra', 'importe_total', 'efectivo', 'comision', 'fecha')
    #raw_id_fields = ('compra',)

    pass
"""
class ProductInline(admin.TabularInline):
     extra = 1
     model = ProductOrder
     verbose_name = "Productos en esta orden"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]
    list_display = ('__str__', 'orden_de_compra', 'order_date', 'total_amount', 'user')


