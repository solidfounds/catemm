from django.contrib import admin
from .models import ComisionEmpleados
# Register your models here.

@admin.register(ComisionEmpleados)
class ComisionEmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'monto', 'liquidado', 'operador')
    filter = ('liquidado')
    pass