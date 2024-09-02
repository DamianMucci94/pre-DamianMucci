from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path("", views.index,name="index"),
    path('pedidos/list', views.pedido_list, name='pedidos_list'),
    path('pedidos/create', views.pedido_create, name='pedidos_create'),
]