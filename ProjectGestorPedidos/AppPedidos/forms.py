from django import forms
from .models import Form_User

class FormularioRegistro(forms.ModelForm):
    class Meta:
        model = Form_User
        fields = ['name', 'company', 'phone_number', 'email', 'interest_areas']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Compañía'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'alguien@example.com'}),
            'interest_areas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Área de Interés'}),
        }
        