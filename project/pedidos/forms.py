from django import forms

from .models import Cliente, Pedido, ProductoCategoria

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(), empty_label="Seleccione un cliente"
    )
    producto = forms.ModelChoiceField(
        queryset=ProductoCategoria.objects.filter(disponible=True), empty_label="Seleccione un producto"
    )

    class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {"fecha_entrega": forms.DateTimeInput(attrs={"type": "datetime-local"})}