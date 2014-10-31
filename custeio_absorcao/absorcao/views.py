from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import  DespesaForm, CustoIndiretoForm
from models import Produto, ProdutoMes, CustoDireto, CustoDiretoProduto, Departamento
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from models import TempoProducao, CustoIndireto, Despesa
from forms import ProdutoForm, TempoProducaoForm


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

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Sua conta esta desabilitada, contacte o administrador do sistema.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('absorcao/login.html', {}, context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def tempo_producao(request):
    context = RequestContext(request)
    context_dict = {}

    tempo_producao = TempoProducao.objects.all()

    context_dict['tempo_producao'] = tempo_producao

    return render_to_response('absorcao/tempo-producao.html', context_dict, context)


def tempo_producao_edit(request, id_tempo):
    context = RequestContext(request)
    context_dict = {}
    try:
        tempo_producao = TempoProducao.objects.get(id=id_tempo)

        context_dict['tempo_producao'] = tempo_producao

    except TempoProducao.DoesNotExist:
        # We get here if we didn't find the specified experiment.
        return render_to_response('absorcao/tempo-producao-edit.html',
                                  context_dict, context)

    if request.POST:
        form = TempoProducaoForm(request.POST, instance=tempo_producao)
        if form.is_valid():

            form.save()

            return HttpResponseRedirect('/tempo-producao/')

        else:
            print form.errors

    else:
        form = TempoProducaoForm(instance=tempo_producao)

    context_dict['form'] = form

    return render_to_response('absorcao/tempo-producao-edit.html', context_dict,
                              context)


def relatorio(request):
    context = RequestContext(request)
    context_dict = {}

    ci = CustoIndireto.objects.all()
    departamentos = Departamento.objects.all()

    context_dict['departamentos'] = departamentos
    context_dict['custeio'] = []
    for idx, custo in enumerate(ci):
        compra = float(custo.porc_compras) * 0.01 * float(custo.valor_mensal)
        almoxarifado = float(custo.porc_almoxarifado) * 0.01 * float(custo.valor_mensal)
        adm_prod = float(custo.porc_adm_prod) * 0.01 * float(custo.valor_mensal)
        corte = float(custo.porc_corte) * 0.01 * float(custo.valor_mensal)
        acabamento = float(custo.porc_acabamento) * 0.01 * float(custo.valor_mensal)
        context_dict['custeio'].append((custo.nome, compra, almoxarifado, adm_prod, corte, acabamento, custo.valor_mensal))

    return render_to_response('absorcao/relatorio.html', context_dict, context)
