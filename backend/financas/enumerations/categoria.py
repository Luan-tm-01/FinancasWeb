from django.db import models

class Categoria(models.TextChoices):
    alimentacao = 'alimentacao', 'Alimentação'
    transporte = 'transporte', 'Transporte'
    moradia = 'moradia', 'Moradia'
    lazer = 'lazer', 'Lazer'
    saude = 'saude', 'Saúde'
    educacao = 'educacao', 'Educação'
    compras = 'compras', 'Compras'
    assinaturas = 'assinaturas', 'Assinaturas'
    contas = 'contas', 'Contas'
    outros = 'outros', 'Outros'