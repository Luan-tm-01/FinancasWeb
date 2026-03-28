from django.shortcuts import render, redirect, get_object_or_404
from .models import TransacaoCompra, TransacaoRecebimento
from .forms import TransacaoCompraForm, TransacaoRecebimentoForm
from django.contrib.auth.decorators import login_required
from django.http import Http404



def index(request):
    return render(request, 'pagina_inicial.html')

@login_required
def listar_transacoes_compras(request):
    transacoes_compras = TransacaoCompra.objects.filter(usuario=request.user)
    return render(request, 'lista_compras.html', {'transacoes_compras': transacoes_compras})

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
def editar_compra(request, compra_id):
    compra = TransacaoCompra.objects.get(id = compra_id)

    form = TransacaoCompraForm(request.POST or None, instance=compra)

    if form.is_valid():
        form.save()
        return redirect ('lista_compras')
    
    return render(request, 'editar_compra.html', {"form": form})

@login_required
def listar_transacoes_recebimentos(request):
    transacoes_recebimentos = TransacaoRecebimento.objects.filter(
        usuario=request.user)
    return render(request, 'lista_recebimentos.html', {'transacoes_recebimentos': transacoes_recebimentos})

@login_required
def criar_transacao_recebimento(request):
    form = TransacaoRecebimentoForm(request.POST or None)

    if form.is_valid():
        recebimento = form.save(commit=False)
        recebimento.usuario = request.user
        recebimento.save()
        return redirect('lista_recebimentos')

    return render(request, 'form_recebimento.html', {'form_recebimento': form})

@login_required
def editar_recebimento(request, recebimento_id):
    recebimento = TransacaoRecebimento.objects.get(id = recebimento_id)

    form = TransacaoRecebimentoForm(request.POST or None, instance=recebimento)

    if form.is_valid():
        form.save()
        return redirect ('lista_recebimentos')
    
    return render(request, 'editar_recebimento.html', {"form": form})
