from django.db import models

class Bancos(models.TextChoices):
    nubank = 'nubank', 'Nubank'
    itau = 'itau', 'Itaú'
    bradesco = 'bradesco', 'Bradesco'
    santander = 'santander', 'Santander'
    bb = 'bb', 'Banco do Brasil'
    caixa = 'caixa', 'Caixa Econômica Federal'
    inter = 'inter', 'Banco Inter'
    c6 = 'c6', 'C6 Bank'
    sicredi = 'sicredi', 'Sicredi'
    banrisul = 'banrisul', 'Banrisul'