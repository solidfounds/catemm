# -*- encoding: utf-8 -*-
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name',)
        widgets={

            'email': forms.TextInput(attrs={'type':'email','id':"email",  'name':"email",'ng-model':"formData.email",'required':'','class': 'form-control ng-pristine ng-invalid ng-invalid-required ng-valid-email', 'placeholder': 'Ingresa tu e-mail',

                                            }),

            'first_name': forms.TextInput(attrs={'type':'text','id':'name' ,'name':'name', 'required':'', 'class':'form-control ng-pristine ng-invalid ng-invalid-required '}),

            'username': forms.TextInput(attrs={'type':'text','id':"username",'ng-model':'formData.name','ng-minlength':'5','ng-maxlength':'20','ng-pattern':'/^[A-z][A-z0-9]*$/','required':'','class': 'form-control ng-pristine ng-invalid ng-invalid-required ng-valid-maxlength ng-valid-minlength ng-valid-pattern'}),



            'password': forms.TextInput(attrs={'type':'password','id':"password",'name':"password",'ng-model':"formData.password",'ng-minlength':'8', 'ng-maxlength':'20','class':'form-control ng-pristine ng-invalid ng-invalid-required ng-valid-maxlength ng-valid-minlength ng-valid-pattern',
                                               'required':'true','minlength':"8",'maxlength':"20",

                                               'ng-pattern':"/(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z])/"}),

        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ingresa tu usuario','required':'true'}))
    password = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'type':'password',
                                                                            'class':'form-control',
                                                                            'placeholder':'ingresa tu contraseña','required':'true'}))

