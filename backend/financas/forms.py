from django import forms
from .models import TransacaoCompra, TransacaoRecebimento, Cartao

class TransacaoCompraForm(forms.ModelForm):
    class Meta:
        model = TransacaoCompra
        fields = '__all__'

class TransacaoRecebimentoForm(forms.ModelForm):
    class Meta:
        model = TransacaoRecebimento
        fields = '__all__'

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = '__all__'