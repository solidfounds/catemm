from django.shortcuts import render, get_object_or_404
from .forms import PrimerRegistroFORM
from django.http import HttpResponseRedirect
from .models import PrimerRegistro, SegundoRegistro, Productos
from  django.core import serializers
import json
from decimal import Decimal


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

def orden_compra(request, cliente_id=None):
    #data = serializers.serialize("json", Productos.objects.all(), fields=('pk', 'name', 'price'))
    cliente =get_object_or_404(PrimerRegistro, id=cliente_id)
    productos = Productos.objects.all()
    #lista = [{'pk':producto.pk, 'name':producto.nombre, 'price': Decimal(producto.precio), } for producto in productos]
    #serializado = json.dumps(lista)
    return render(request,'odc.html', { 'productos':productos,
                                        'cliente':cliente,
                                        #'data':data,
                                       #'lista':serializado,
                                       } )
