from django.db import models

class TipoPagamentos(models.TextChoices):
    dinheiro = 'dinheiro', 'Dinheiro'
    cartao = 'cartao', 'Cartão'
    voucher = 'voucher', 'Voucher'
    