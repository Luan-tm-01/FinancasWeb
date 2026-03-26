from django.contrib import admin
from .models import Categoria, Cartao, TransacaoCompra, TransacaoRecebimento

admin.site.register(Categoria)
admin.site.register(Cartao)
admin.site.register(TransacaoCompra)
admin.site.register(TransacaoRecebimento)
