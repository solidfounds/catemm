from django.shortcuts import render, get_object_or_404
from .forms import PrimerRegistroFORM,SegundoRegistroForm
from django.http import HttpResponseRedirect
from .models import PrimerRegistro, SegundoRegistro, Productos
from users.models import User
from  django.core import serializers
import json
from decimal import Decimal


# Create your views here.


def index(request):

    return render(request, 'index.html',{ 'mis_clientes':mis_clientes,})

def nota_remision(request):
    return render(request, 'nota-remision.html')

def clientes(request):
    usuario = request.user
    cliente = PrimerRegistro.objects.filter(operador__username__contains = usuario)
    clienta = PrimerRegistro.objects.filter(operador__username__contains=usuario)
    tarjeta = SegundoRegistro.objects.filter(operador__username__contains= usuario)
    return render(request, 'clientes.html', {
        'cliente': cliente,
        'clienta': clienta,
        'tarjeta': tarjeta,
    })


def desempeno(request):
    usuario = request.user
    mi_info = User.objects.get(username = usuario)
    total_clientes = PrimerRegistro.objects.filter(operador__username__contains= usuario).count()
    return render(request, 'desempeno.html', {'mi_info':mi_info,'total_clientes':total_clientes})



def primerRegistro(request):
    usuario = request.user
    if request.method == 'POST':
            form = PrimerRegistroFORM(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.operador = request.user
                post.save()
                return HttpResponseRedirect('/desempeno/')
    else:
        form = PrimerRegistroFORM()

    mis_clientes = PrimerRegistro.objects.filter(operador__username__contains=usuario)
    return render(request,'index.html',{'form':form, 'mis_clientes':mis_clientes} )


def segundoRegistro(request):
    usuario = request.user
    if request.method == 'POST':
        form = SegundoRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            posta = form.save(commit=False)
            posta.operador = request.user
            posta.save()
            return HttpResponseRedirect('/desempeno/')
    else:
        form = SegundoRegistroForm()
    mis_clientes = SegundoRegistro.objects.filter(operador__username__contains=usuario)
    return render(request, 'segundo-registro.html', {'form':form, 'mis_clientes':mis_clientes})

def orden_compra1(request, cliente_id=None):
    #data = serializers.serialize("json", Productos.objects.all(), fields=('pk', 'name', 'price'))
    cliente =get_object_or_404(PrimerRegistro, id=cliente_id)
    productos = Productos.objects.all()
    #lista = [{'pk':producto.pk, 'name':producto.nombre, 'price': Decimal(producto.precio), } for producto in productos]
    #serializado = json.dumps(lista)
    return render(request, 'odc/odc1.html', { 'productos':productos,
                                        'cliente':cliente,
                                        #'data':data,
                                       #'lista':serializado,
                                       } )
def orden_compra2(request, cliente_id=None):
    #data = serializers.serialize("json", Productos.objects.all(), fields=('pk', 'name', 'price'))
    cliente =get_object_or_404(PrimerRegistro, id=cliente_id)
    productos = Productos.objects.all()
    #lista = [{'pk':producto.pk, 'name':producto.nombre, 'price': Decimal(producto.precio), } for producto in productos]
    #serializado = json.dumps(lista)
    return render(request,'odc/odc2.html', { 'productos':productos,
                                        'cliente':cliente,
                                        #'data':data,
                                       #'lista':serializado,
                                       } )

def orden_compra3(request, cliente_id=None):
    #data = serializers.serialize("json", Productos.objects.all(), fields=('pk', 'name', 'price'))
    cliente =get_object_or_404(PrimerRegistro, id=cliente_id)
    productos = Productos.objects.all()
    #lista = [{'pk':producto.pk, 'name':producto.nombre, 'price': Decimal(producto.precio), } for producto in productos]
    #serializado = json.dumps(lista)
    return render(request,'odc/odc3.html', { 'productos':productos,
                                        'cliente':cliente,
                                        #'data':data,
                                       #'lista':serializado,
                                       } )