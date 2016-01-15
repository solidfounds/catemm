from django.shortcuts import render
from .forms import PrimerRegistroFORM
from django.http import HttpResponseRedirect
from .models import PrimerRegistro, SegundoRegistro


# Create your views here.


def index(request):
    return render(request, 'index.html')

def nota_remision(request):
    return render(request, 'nota-remision.html')

def clientes(request):
    usuario = request.user
    cliente = PrimerRegistro.objects.all().filter(operador = usuario)
    tarjeta = SegundoRegistro.objects.all().filter(operador = usuario)
    return render(request, 'clientes.html', {
        'cliente': cliente,
        'tarjeta': tarjeta,
    })


def desempeno(request):
    return render(request, 'desempeno.html')



def primerRegistro(request):
    if request.method == 'POST':
            form = PrimerRegistroFORM(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.operador = request.user
                post.save()
                return HttpResponseRedirect('/desempeno/')
    else:
        form = PrimerRegistroFORM()
    return render(request,'index.html',{'form':form} )