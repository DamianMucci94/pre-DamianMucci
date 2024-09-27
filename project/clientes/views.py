from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ClienteForm, PaisForm
from .models import Cliente, Pais

@login_required
def index(request):
    return render(request, 'clientes/index.html')

def pais_list(request):
    q = request.GET.get('q')
    if q:
        query = Pais.objects.filter(nombre__icontains=q)
    else:
        query = Pais.objects.all()
    contexto = {'object_list': query}
    return render(request, 'clientes/pais_list.html', contexto)

def pais_create(request):
    if request.method == 'GET':
        form = PaisForm()
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('clientes:pais_list')
    return render(request, 'clientes/pais_create.html', {'form': form})

def pais_detail(request, pk: int):
    query = Pais.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'clientes/pais_detail.html', context)

class PaisUpdate(UpdateView):
    model = Pais
    form_class = PaisForm
    success_url = reverse_lazy('clientes:pais_list')
    template_name = 'clientes/pais_create.html'

class PaisDelete(DeleteView):
    model = Pais
    success_url = reverse_lazy('clientes:pais_list')

def cliente_list(request):
    q = request.GET.get('q')
    if q:
        query = Cliente.objects.filter(nombre__icontains=q)
    else:
        query = Cliente.objects.all()    
    contexto = {'object_list': query}
    return render(request, 'clientes/cliente_list.html', contexto)

def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:cliente_list")
    return render(request, "clientes/cliente_create.html", {"form": form})

class ClienteDetail(DetailView):
    model = Cliente

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:clientes_list')
    template_name = 'clientes/cliente_create.html'

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:clientes_list')