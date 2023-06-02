import json
import pandas as pd
import xlwt
#nuevas importaciones 30-05-2022
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from registration.models import Profile
from ordencompra.models import OrdenCompra, ItemOrden
from product.models import Producto
from prov.models import Proveedor

#fin nuevas importaciones 30-05-2022

from django.db.models import Count, Avg, Q
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import (
	api_view, authentication_classes, permission_classes)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


def crear_orden_compra(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        producto_id = request.POST.get('producto')
        producto = get_object_or_404(Producto, id=producto_id)
        cantidad = int(request.POST.get('cantidad'))
        orden_compra = OrdenCompra.objects.create(proveedor=proveedor)
        item = ItemOrden.objects.create(orden_compra=orden_compra, producto=producto, cantidad=cantidad)
        producto.stock += cantidad
        producto.save()
        return redirect('ver_orden_compra', orden_id=orden_compra.id)
    
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'ordencompra/crear_orden_compra.html', {'proveedores': proveedores, 'productos': productos})


def ver_orden_compra(request, orden_id):
    orden = get_object_or_404(OrdenCompra, id=orden_id)
    return render(request, 'ordencompra/ver_orden_compra.html', {'orden': orden})


def eliminar_orden_compra(request, orden_id):
    orden = get_object_or_404(OrdenCompra, id=orden_id)
    orden.delete()
    return redirect('listar_ordenes_compra')


def listar_ordenes_compra(request):
    ordenes = OrdenCompra.objects.all()
    return render(request, 'ordencompra/listar_ordenes_compra.html', {'ordenes': ordenes})


def agregar_item(request, orden_id):
    if request.method == 'POST':
        orden = get_object_or_404(OrdenCompra, id=orden_id)
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))
        producto = get_object_or_404(Producto, id=producto_id)
        item = ItemOrden.objects.create(orden_compra=orden, producto=producto, cantidad=cantidad)
        producto.stock += cantidad
        producto.save()
        return redirect('ver_orden_compra', orden_id=orden.id)
    else:
        orden = get_object_or_404(OrdenCompra, id=orden_id)
        productos = Producto.objects.all()
        return render(request, 'ordencompra/agregar_item.html', {'orden': orden, 'productos': productos})


def eliminar_item(request, item_id):
    item = get_object_or_404(ItemOrden, id=item_id)
    orden_id = item.orden_compra.id
    item.delete()
    return redirect('ver_orden_compra', orden_id=orden_id)

def order_main(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ordencompra/order_main.html'
    return render(request,template_name,{'profile':profile})
