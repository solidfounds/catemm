from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login
from django.views.generic import FormView
from app import models
from .functions import LogIn
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm, LoginForm
from .models import User


class userlogin(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('agregar_clientes')

    def form_valid(self, form):
        user = authenticate(
        username = form.cleaned_data['username'],
        password = form.cleaned_data['password']
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(userlogin, self).form_valid(form)

# def userlogin(request):
#     if request.method == 'POST':
#         if 'register_form' in request.POST:
#              user_register = UserRegisterForm(request.POST)
#              if user_register.is_valid():
#                  User.objects.create_user(username=user_register.cleaned_data['username'],
#                                           email=user_register.cleaned_data['email'],
#                                           password=user_register.cleaned_data['password'],
#                                           first_name=user_register.cleaned_data['first_name'])
#                  LogIn(request, user_register.cleaned_data['username'],user_register.cleaned_data['password'])
#                  return redirect('home')
#         if 'login_form' in request.POST:
#             login_form = LoginForm(request.POST)
#             if login_form.is_valid():
#                 LogIn(request, login_form.cleaned_data['username'],
#                         login_form.cleaned_data['password'])
#                 return redirect('/')
#
#     else:
#         user_register = UserRegisterForm()
#         login_form = LoginForm()
#      return render(request, 'login.html', {'login_form': login_form })





def LogOut(request):
    logout(request)
    return redirect('/')