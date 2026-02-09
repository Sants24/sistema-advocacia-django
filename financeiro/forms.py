from django import forms
from .models import Honorario

class HonorarioForm(forms.ModelForm):
    class Meta:
        model = Honorario
        fields = ['cliente', 'descricao', 'valor', 'data_vencimento', 'status', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Honorários Causa Trabalhista'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'data_vencimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }