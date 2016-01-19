# -*- encoding: utf-8 -*-
from .models import PrimerRegistro, SegundoRegistro
from django import forms
from django.forms import ModelForm

class PrimerRegistroFORM(ModelForm):
    class Meta:
        model = PrimerRegistro
        fields = ('nombre', 'apellidos', 'direccion', 'nsn','telefono','empresa','registro_patronal','comision','ife','email','numero_de_cuenta','banco')
        #exclude = ['operador_que_lo_registro',]
        widgets={
            'nombre': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm  col-md-2'}),
            'apellidos': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm  col-md-2'}),
            'direccion': forms.Textarea(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'nsn': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'telefono': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm'}),
            'empresa': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'registro_patronal': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),
            'comision': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm'}),
            'ife': forms.ClearableFileInput(attrs={'type':'file','required':'true','class':' form-control-sm'}),
            'email': forms.EmailInput(attrs={'type':'email','required':'true','class':'form-control form-control-sm'}),
            'numero_de_cuenta': forms.TextInput(attrs={'type':'number','required':'true','class':'form-control form-control-sm'}),
            'banco': forms.TextInput(attrs={'type':'text','required':'true','class':'form-control form-control-sm'}),

        }

class SegundoRegistroForm(ModelForm):
    class Meta:
        model = SegundoRegistro
        fields = ('cliente', 'caratula', 'tarjeta_de_mejoravit', 'numero_tarjeta', 'tarjeta_entregada', 'tarjeta_activa', 'tarjeta_con_fondos', 'credito',)




