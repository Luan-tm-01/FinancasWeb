from django.contrib import admin
from .models import TransacaoCompra, TransacaoRecebimento

admin.site.register(TransacaoCompra)
admin.site.register(TransacaoRecebimento)
