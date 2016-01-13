# -*- encoding: utf-8 -*-
from .models import PrimerRegistro
from django import forms
from django.forms import ModelForm

class PrimerRegistroFORM(ModelForm):
    class Meta:
        model = PrimerRegistro
        fields = ('nombre', 'apellidos', 'direccion', 'nsn','telefono_casa','telefono_celular','empresa','registro_patronal','facturacion','comision','acta_de_nacimiento','ife','email',)
        widgets={
            'nombre': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control'}),
            'direccion': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control'}),
            'nsn': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control'}),
            'telefono_casa': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control'}),
            'telefono_celular': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control'}),
            'empresa': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control'}),
            'registro_patronal': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control'}),
            'facturacion': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control'}),
            'comision': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control'}),
            'ife': forms.TextInput(attrs={'type':'file','required':'true','class':''}),
            'email': forms.TextInput(attrs={'type':'email','required':'true','class':'form-control'}),
        }




