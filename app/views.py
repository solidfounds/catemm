from itertools import chain
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PrimerRegistroFORM,SegundoRegistroForm, OrderForm
from django.http import HttpResponseRedirect
from .models import PrimerRegistro, SegundoRegistro, Productos, ProductOrder, Order
from users.models import User
from  django.core import serializers
import json
from decimal import Decimal


# Create your views here.


def index(request):

    return render(request, 'index.html',)

def nota_remision(request):
    return render(request, 'nota-remision.html')

def clientes(request):
    usuario = request.user
    cliente = PrimerRegistro.objects.filter(operador__username__contains = usuario)

    tarjeta = SegundoRegistro.objects.filter(operador__username__contains= usuario)
    ordenes = Order.objects.filter(operador__username__contains= usuario)
    orden1 = Order.objects.filter(Q(orden_de_compra = "1") & Q(operador__username__contains= usuario))
    orden2 = Order.objects.filter(Q(orden_de_compra = "2") & Q(operador__username__contains= usuario))
    orden3 = Order.objects.filter(Q(orden_de_compra = "3") & Q(operador__username__contains= usuario))
    return render(request, 'clientes.html', {
        'cliente': cliente,
        'tarjeta': tarjeta,
        'ordenes': ordenes,
        'orden1': orden1,
        'orden2': orden2,
        'orden3': orden3,
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
            post.operador = usuario
            post.save()
            return redirect('agregar_clientes')
    else:
        form = PrimerRegistroFORM()
    mis_clientes = PrimerRegistro.objects.filter(operador__username__contains=usuario)
    return render(request,'index.html',{'form':form, 'mis_clientes':mis_clientes} )

def PrimerRegistroEdit(request, pk, template_name='editar/primer_registro.html'):
    clientes = get_object_or_404(PrimerRegistro, pk=pk)
    form  = PrimerRegistroFORM(request.POST or None,  instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('agregar_clientes')
    return render(request, template_name, {'form':form})

def PrimerRegistroDelete(request, pk, template_name='delete/confirmacion.html'):
    clientes = get_object_or_404(PrimerRegistro, pk=pk)
    if request.method=='POST':
        clientes.delete()
        return redirect('agregar_clientes')
    return render(request, template_name, {'object':clientes})

def segundoRegistro(request):
    usuario = request.user
    if request.method == 'POST':
        form = SegundoRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            posta = form.save(commit=False)
            posta.operador = usuario
            posta.save()
            return redirect('segundo_registro')
    else:
        form = SegundoRegistroForm()
    mis_clientes = SegundoRegistro.objects.filter(operador__username__contains=usuario)
    return render(request, 'segundo-registro.html', {'form':form, 'mis_clientes':mis_clientes})

def SegundoRegistroEdit(request, pk, template_name='editar/segundo_registro.html'):
     clientes = get_object_or_404(SegundoRegistro, pk=pk)
     form  = SegundoRegistroForm(request.POST or None,  instance=clientes)
     if form.is_valid():
         form.save()
         return redirect('segundo_registro')
     return render(request, template_name, {'form':form})


def SegundoRegistroDelete(request, pk, template_name='delete/confirmacion2.html'):
     clientes = get_object_or_404(SegundoRegistro, pk=pk)
     if request.method=='POST':
         clientes.delete()
         return redirect('segundo_registro')
     return render(request, template_name, {'object':clientes})



def orden_compra1(request, cliente_id=None):
    #data = serializers.serialize("json", Productos.objects.all(), fields=('pk', 'name', 'price'))

    if  Order.objects.filter(Q(user__id=cliente_id)& Q(orden_de_compra=1)).exists():
        ordencliente = Order.objects.filter(Q(user__id=cliente_id)&Q(orden_de_compra=1))
        productos = ProductOrder.objects.filter(order =ordencliente )
        return render(request, 'odc/odc1-echa.html',{'ordencliente':ordencliente,
                                                     'productos':productos})

    else:
        cliente =get_object_or_404(PrimerRegistro, id=cliente_id)
        productos = Productos.objects.all()
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                user = cliente
                order_content = json.loads(request.POST['cartJSONdata'])
                order = form.save(commit=False)
                order.user = user
                order.operador = request.user
                order.total_amount = 0
                order.save()   #We have to save the order before calculate ammount
                order.total_amount = saveOrderProducts(order_content, order)
                order.save()
                books = ProductOrder.objects.filter(order=order)
                products = list(chain( books,))
                return redirect('/')
                #return render(request, 'success.html', locals())
        else:
            form = OrderForm()
        #lista = [{'pk':producto.pk, 'name':producto.nombre, 'price': Decimal(producto.precio), } for producto in productos]
        #serializado = json.dumps(lista)
        return render(request, 'odc/odc1.html', { 'productos':productos,
                                            'cliente':cliente,
                                            'form': form,
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

def saveOrderProducts(order_content, order):
    amount = 0
    prod_error = False
    for product in order_content:
        product_uid = product['id']
        quantity = product['quantity']
        p_price = product['price']
        amount += float(p_price) * float(quantity)
        product_obj = Productos.objects.get(pk=product_uid)
        product_obj.save()
        prod_order = order.productorder_set.create(product=product_obj, quantity=quantity)

        if not prod_error:
            prod_order.save()
    return amount







