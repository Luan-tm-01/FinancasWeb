from django import forms
from .models import TransacaoCompra, TransacaoRecebimento

class TransacaoCompraForm(forms.ModelForm):
    class Meta:
        model = TransacaoCompra
        exclude = ['usuario']  

class TransacaoRecebimentoForm(forms.ModelForm):
    class Meta:
        model = TransacaoRecebimento
        exclude = ['usuario']  