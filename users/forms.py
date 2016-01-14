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


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username' : forms.TextInput(attrs={
                    'class' : 'input input-username',
                    'required': True,
                    'type': 'text',
                    'placeholder': 'Ingresa tu nombre de usuario'
                }),
            'password' : forms.TextInput(attrs={
                    'class' : 'input',
                    'type' : 'password',
                    'required': True,
                    'placeholder': 'Ingresa tu contraseña'
                })
        }

    def clean(self):
        if not User.objects.filter(username = self.cleaned_data.get('username')).exists():
            self.add_error('username', 'El nombre de usuario no esta registrado')
        else:
            user = User.objects.get(username = self.cleaned_data.get('username'))
            if not user.check_password(self.cleaned_data.get('password')):
                self.add_error('username', 'La contraseña es incorrecta')

# class LoginForm(forms.Form):
#
#     username = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ingresa tu usuario','required':'true'}))
#     password = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'type':'password',
#                                                                             'class':'form-control',
#                                                                             'placeholder':'ingresa tu contraseña','required':'true'}))
#     def clean(self):
#             if not User.objects.filter(username = self.cleaned_data['username']).exists():
#                 self.add_error('username', 'El nombre de usuario no existe')
#             else:
#                 user = User.objects.get(username = self.cleaned_data['username'])
#                 if not user.check_password(self.cleaned_data['password']):
#                     self.add_error('username', 'El password es incorrecto')
