from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import Cliente, Pais


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
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
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {'nacimiento': forms.DateInput(attrs={'type': 'date'})}
    
    def clean_nacimiento(self):
        nacimiento = self.cleaned_data.get('nacimiento', '')

        if isinstance(nacimiento, str):  # Verifica si el dato es una cadena
            try:
                # Intenta convertir la cadena a un objeto de tipo date
                nacimiento = datetime.strptime(nacimiento, '%d-%m-%Y').date()
            except ValueError:
                # Si la conversión falla, levanta una excepción de validación
                raise ValidationError('Formato de fecha incorrecto. Usa DD-MM-YYYY.')
        return nacimiento