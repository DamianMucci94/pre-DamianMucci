from django.shortcuts import render

from .models import ProductoCategoria


def index(request):
    return render(request, 'productos/index.html')


def productocategoria_list(request):
    productocategoria = ProductoCategoria.objects.all()
    contexto = {'productocategoria': productocategoria}
    return render(request, 'productos/productocategoria_list.html', contexto)