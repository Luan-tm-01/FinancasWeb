from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='pagina_inicial'),
    path('compras/', listar_transacoes_compras, name='lista_compras'),
    path('recebimentos/', listar_transacoes_recebimentos, name='lista_recebimentos'),
    path('compras/nova/', criar_transacao_compra, name='nova_compra'),
    path('compras/<compra_id>', views.editar_compra, name= 'editar_compra'),
    path('recebimentos/nova/', criar_transacao_recebimento, name='novo_recebimento'),
    path('recebimentos/<recebimento_id>', views.editar_recebimento, name= 'editar_recebimento'),
]