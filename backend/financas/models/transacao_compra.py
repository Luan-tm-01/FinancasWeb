from .base_model import *
from django.contrib.auth.models import User
from financas.models import Categoria, Cartao
from financas.enumerations import TipoPagamentos

class TransacaoCompra(BaseModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    tipo_pagamento = models.CharField(max_length=20, choices=TipoPagamentos)
    cartao = models.ForeignKey(Cartao, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Transações | Compras"

    def __str__(self):
        return f'Gastou R${self.valor} no Dia {self.data}'