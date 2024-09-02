from django.shortcuts import render, redirect

from .models import Pedido
from .forms import PedidoForm

def index(request):
    return render(request, 'pedidos/index.html')

def pedido_list(request):
    pedidos = Pedido.objects.all()
    contexto = {"pedidos": pedidos}
    return render(request, "pedidos/pedido_list.html", contexto)

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "pedidos/pedido_create.html", {"form": form})
