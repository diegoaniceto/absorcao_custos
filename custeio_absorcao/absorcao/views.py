from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Produto, ProdutoMes, CustoIndireto,Despesa
from forms import ProdutoForm, DespesaForm, CustoIndiretoForm


def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('absorcao/index.html', context_dict, context)


def despesas_index(request):
    context = RequestContext(request)
    context_dict = {}

    despesas = Despesa.objects.all()

    context_dict['despesas'] = despesas

    return render_to_response('absorcao/despesas.html', context_dict, context)

def despesa_edit(request, id_despesa=None):
    context = RequestContext(request)
    context_dict = {}
    try:
        despesa = Despesa.objects.get(id=id_despesa)

        context_dict['despesa'] = despesa

    except Despesa.DoesNotExist:
        # We get here if we didn't find the specified experiment.
        return render_to_response('absorcao/despesas-edit.html',
                                  context_dict, context)

    if request.POST:
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():

            form.save()

            # If the save was successful, redirect to the details page
            return HttpResponseRedirect('/despesas/')

        else:
            print form.errors

    else:
        form = DespesaForm(instance=despesa)

    context_dict['form'] = form

    return render_to_response('absorcao/despesas-edit.html', context_dict,
                              context)


def custo_indireto_index(request):
    context = RequestContext(request)
    context_dict = {}

    custos_indiretos = CustoIndireto.objects.all()

    context_dict['custos_indiretos'] = custos_indiretos

    return render_to_response('absorcao/custo-indireto.html', context_dict, context)


def custo_indireto_edit(request, id_custo_indireto=None):
    context = RequestContext(request)
    context_dict = {}
    try:
        custo_indireto = CustoIndireto.objects.get(id=id_custo_indireto)

        context_dict['custo_indireto'] = custo_indireto

    except CustoIndireto.DoesNotExist:
        # We get here if we didn't find the specified experiment.
        return render_to_response('absorcao/custo-indireto-edit.html',
                                  context_dict, context)

    if request.POST:
        form = CustoIndiretoForm(request.POST, instance=custo_indireto)
        if form.is_valid():

            form.save()

            # If the save was successful, redirect to the details page
            return HttpResponseRedirect('/custo-indireto/')

        else:
            print form.errors

    else:
        form = CustoIndiretoForm(instance=custo_indireto)

    context_dict['form'] = form

    return render_to_response('absorcao/custo-indireto-edit.html', 
                        context_dict, context)



def produto_edit(request, id_produto=None):
    context = RequestContext(request)
    context_dict = {}
    try:
        custo_indireto = CustoIndireto.objects.get(id=id_produto)

        context_dict['custo_indireto'] = custo_indireto

    except Produto.DoesNotExist:
        # We get here if we didn't find the specified experiment.
        return render_to_response('absorcao/custo-indireto-edit.html',
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

