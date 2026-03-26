from django.shortcuts import render, redirect
from .models import TransacaoCompra, TransacaoRecebimento
from .forms import TransacaoCompraForm, TransacaoRecebimentoForm, CartaoForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'pagina_inicial.html')

@login_required
def listar_transacoes_compras(request):
    transacoes_compras = TransacaoCompra.objects.filter(usuario = request.user)
    return render(request, 'lista_compras.html', {'transacoes_compras': transacoes_compras})

@login_required
def listar_transacoes_recebimentos(request):
    transacoes_recebimentos = TransacaoRecebimento.objects.filter(usuario=request.user)
    return render(request, 'lista_recebimentos.html', {'transacoes_recebimentos': transacoes_recebimentos})

@login_required
def criar_transacao_compra(request):
    form_compra = TransacaoCompraForm(request.POST or None)

    if form_compra.is_valid():
        transacao = form_compra.save(commit=False)
        transacao.usuario = request.user 
        transacao.save()
        return redirect('lista_compras')

    return render(request, 'form_compra.html', {'form_compra': form_compra})

@login_required
def criar_transacao_recebimento(request):
    form_recebimento = TransacaoRecebimentoForm(request.POST or None)

    if form_recebimento.is_valid():
        transacao = form_recebimento.save(commit=False)
        transacao.usuario = request.user  
        transacao.save()
        return redirect('lista_recebimentos')

    return render(request, 'form_recebimento.html', {'form_recebimento': form_recebimento})

@login_required
def criar_cartao(request):
    form_cartao = CartaoForm(request.POST or None)

    if form_cartao.is_valid():
        cartao = form_cartao.save(commit=False)
        cartao.usuario = request.user
        cartao.save()
        return redirect('lista_compras')

    return render(request, 'form_cartao.html', {'form_cartao': form_cartao})