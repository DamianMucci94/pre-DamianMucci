from django.shortcuts import render, redirect

from .forms import ClienteForm
from .models import Cliente, Pais

def index(request):
    return render(request, 'clientes/index.html')

def pais_list(request):
    paises = Pais.objects.all()
    contexto = {'paises': paises}
    return render(request, 'clientes/pais_list.html', contexto)

def cliente_list(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'clientes/cliente_list.html', contexto)

def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    return render(request, "clientes/cliente_create.html", {"form": form})