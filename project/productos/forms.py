from django import forms
from django.core.exceptions import ValidationError

from .models import ProductoCategoria


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria
        # fields = ['nombre', 'descripcion']
        fields = '__all__'

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get('nombre', '')

        # Validar que solo contenga letras
        if not nombre.isalpha():
            raise ValidationError('El nombre sólo puede contener letras')

        # Validar longitud de nombre
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValidationError(
                'El nombre debe tener una longitud mínima de 3 letras o máxima de 50'
            )
        return nombre