from django.shortcuts import render
from .forms import PrimerRegistroFORM

# Create your views here.


def index(request):
	return render(request, 'index.html')

def nota_remision(request):
	return render(request, 'nota-remision.html')

def clientes(request):
	return render(request, 'clientes.html')


def desempeno(request):
	return render(request, 'desempeno.html')

def primerRegistro(request):
	form = PrimerRegistroFORM()
	return render(request,'index.html',{'form':form} )