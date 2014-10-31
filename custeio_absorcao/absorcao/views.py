from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Produto, ProdutoMes, CustoDireto, CustoDiretoProduto
from forms import ProdutoForm


def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('absorcao/index.html', context_dict, context)


def produto_index(request):
    context = RequestContext(request)
    context_dict = {}

    produtos = Produto.objects.all()

    context_dict['produtos'] = produtos

    return render_to_response('absorcao/produto.html', context_dict, context)


def produto_edit(request, id_produto=None):
    context = RequestContext(request)
    context_dict = {}
    try:
        produto = Produto.objects.get(id=id_produto)

        context_dict['produto'] = produto

    except Produto.DoesNotExist:
        # We get here if we didn't find the specified experiment.
        return render_to_response('absorcao/produto-edit.html',
                                  context_dict, context)

    if request.POST:
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():

            form.save()

            # If the save was successful, redirect to the details page
            return HttpResponseRedirect('/produto/')

        else:
            print form.errors

    else:
        form = ProdutoForm(instance=produto)

    context_dict['form'] = form

    return render_to_response('absorcao/produto-edit.html', context_dict,
                              context)


def produto_view(request, id_produto=None):
    context = RequestContext(request)
    context_dict = {}
    try:
        produto = Produto.objects.get(id=id_produto)
        produto_meses = ProdutoMes.objects.filter(produto=produto)

        context_dict['produto'] = produto
        context_dict['produto_meses'] = produto_meses

    except Produto.DoesNotExist:
        # We get here if we didn't find the specified experiment.
        return render_to_response('absorcao/produto-view.html',
                                  context_dict, context)

    return render_to_response('absorcao/produto-view.html', context_dict,
                              context)

def custo_direto_index(request):
    context = RequestContext(request)
    context_dict = {}
    
    custos_diretos = CustoDireto.objects.all().order_by('nome')
    produtos = Produto.objects.all().order_by('nome')
    custos_diretos_produtos = CustoDiretoProduto.objects.all().order_by('produto__nome').order_by('custo_direto__nome')
    
    context_dict['custos_diretos'] = custos_diretos
    context_dict['produtos'] = produtos
    context_dict['custos_diretos_produtos'] = custos_diretos_produtos
    
    return render_to_response('absorcao/custo_direto.html', context_dict, context)

def custo_direto_edit(request, mes=None):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('absorcao/custo_direto-edit.html', context_dict, context)
