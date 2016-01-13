# -*- encoding: utf-8 -*-
from .models import PrimerRegistro
from django import forms
from django.forms import ModelForm

class PrimerRegistroFORM(ModelForm):
    class Meta:
        model = PrimerRegistro
        fields = ('nombre', 'apellidos', 'direccion', 'nsn','telefono_casa','telefono_celular','empresa','registro_patronal','facturacion','comision','acta_de_nacimiento','ife','email',)
        widgets={
            'nombre': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm  col-md-2'}),
            'apellidos': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm  col-md-2'}),
            'direccion': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'nsn': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'telefono_casa': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm'}),
            'telefono_celular': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm'}),
            'empresa': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'registro_patronal': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'facturacion': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'comision': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm'}),
            'ife': forms.TextInput(attrs={'type':'file','required':'true','class':' form-control-sm'}),
            'email': forms.TextInput(attrs={'type':'email','required':'true','class':'form-control form-control-sm'}),
        }




