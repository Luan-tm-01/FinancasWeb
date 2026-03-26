from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='pagina_inicial'),
    path('compras/', listar_transacoes_compras, name='lista_compras'),
    path('recebimentos/', listar_transacoes_recebimentos, name='lista_recebimentos'),
    path('compras/nova/', criar_transacao_compra, name='nova_compra'),
    path('recebimentos/nova/', criar_transacao_recebimento, name='novo_recebimento'),
    path('cartao/', criar_cartao, name='cartao'),
]