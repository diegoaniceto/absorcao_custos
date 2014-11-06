from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import DespesaForm, CustoIndiretoForm
from models import Produto, ProdutoMes, CustoDireto, CustoDiretoProduto
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from models import TempoProducao, CustoIndireto, Despesa
from models import Departamento
from models import Mes
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

# DRE =================================


def dre(request):
    context = RequestContext(request)
    context_dict = {}

    NOME_INDEX = 0
    CAMISETAS_INDEX = 1
    VESTIDOS_INDEX = 2
    CALCAS_INDEX = 3
    TOTAL_INDEX = 4

    # Vendas
    vendas = [0, 0, 0, 0, 0]
    vendas[CAMISETAS_INDEX] = vendas_mes(03, 2014, 'Camisetas')
    vendas[VESTIDOS_INDEX] = vendas_mes(03, 2014, 'Vestidos')
    vendas[CALCAS_INDEX] = vendas_mes(03, 2014, 'Calcas')
    vendas[TOTAL_INDEX] = sum(vendas)
    vendas[NOME_INDEX] = 'Vendas'

    # Custo de Produtos Vendidos
    cpv = [0, 0, 0, 0, 0]
    cpv[CAMISETAS_INDEX] = custo_produto_vendido(03, 2014, 'Camisetas')
    cpv[VESTIDOS_INDEX] = custo_produto_vendido(03, 2014, 'Vestidos')
    cpv[CALCAS_INDEX] = custo_produto_vendido(03, 2014, 'Calcas')
    cpv[TOTAL_INDEX] = sum(cpv)
    cpv[NOME_INDEX] = 'Custos dos Produtos Vendidos'

    context_dict['vendas'] = vendas
    context_dict['cpv'] = cpv

    return render_to_response('absorcao/dre.html', context_dict, context)


def custo_produto_vendido(num_mes, ano, nome_produto):
    mes = Mes.objects.get(ano=ano, numero=num_mes)
    produto = Produto.objects.get(nome=nome_produto)
    produto_mes = ProdutoMes.objects.get(produto=produto, mes=mes)
    produto_mes.quantidade_vendas = produto_mes.producao_mensal  # FIX ME
    print custo_total_unitario(mes, produto)
    return custo_total_unitario(mes, produto) * produto_mes.quantidade_vendas


# custo total * quantidade vendida = CPV
# Deve ser 6.83 para camisetas
def custo_total_unitario(mes, produto):
    custo_dir = custo_direto_unitario_total(produto, mes)
    custo_indir = custo_indireto_unitario_total(produto)
    return float(custo_dir) + custo_indir


# Custo indireto unitario total + custo direto unitario total = Custo total
# Eh a soma dos custos indiretos por departamento
def custo_indireto_unitario_total(produto):
    deptos = Departamento.objects.filter(producao=True)
    total = 0
    for d in deptos:
        total += custo_indireto_unitario_por_depto(produto, d)
    return total


def custo_indireto_unitario_por_depto(produto, departamento):
    tempo_producao = TempoProducao.objects.get(produto=produto, departamento=departamento)
    #tempo_producao.tempo_unitario  deve ser 0.3 para camisa e corte e costura
    print '--' + str(custo_por_hora(departamento))
    print tempo_producao.tempo_unitario
    return custo_por_hora(departamento) * float(tempo_producao.tempo_unitario)


# Deve ser 3.75 pra camiseta OK!
# Custo indireto unitario total + custo direto unitario total = Custo total
def custo_direto_unitario_total(produto, mes):
    custo_dir_produto = CustoDiretoProduto.objects.filter(produto=produto, mes=mes)
    custo_dir_total = 0
    for custo_dir in custo_dir_produto:
        custo_dir_total += custo_dir.valor_unitario
    return custo_dir_total


def vendas_mes(num_mes, ano, nome_produto):
    mes = Mes.objects.get(numero=num_mes, ano=ano)
    produto = Produto.objects.get(nome=nome_produto)
    produto_mes = ProdutoMes.objects.get(mes=mes, produto=produto)
    produto_mes.quantidade_vendas = produto_mes.producao_mensal
    return produto_mes.preco_venda_unitario * produto_mes.quantidade_vendas


def custo_por_hora(departamento):
    todas_variaveis = faz_rateio_e_muito_mais()
    custo_hora = todas_variaveis[9]
    CORTE_INDEX = 3
    ACABAMENTO_INDEX = 4
    if departamento.nome == 'Corte e Costura':
        return custo_hora[CORTE_INDEX]
    else:
        return custo_hora[ACABAMENTO_INDEX]

# RELATORIO =================================


def relatorio(request):
    context = RequestContext(request)
    context_dict = {}
    
    todas_variaveis = faz_rateio_e_muito_mais()

    context_dict['custeio'] = todas_variaveis[0]
    context_dict['subtotal1'] = todas_variaveis[1]
    context_dict['rateio_compras'] = todas_variaveis[2]
    context_dict['subtotal2'] = todas_variaveis[3]
    context_dict['rateio_almox'] = todas_variaveis[4]
    context_dict['subtotal3'] = todas_variaveis[5]
    context_dict['rateio_adm'] = todas_variaveis[6]
    context_dict['total_depts_prod'] = todas_variaveis[7]
    context_dict['horas_prod'] = todas_variaveis[8]
    context_dict['custo_hora'] = todas_variaveis[9]
    return render_to_response('absorcao/relatorio.html', context_dict, context)


def faz_rateio_e_muito_mais():
    COMPRAS_INDEX = 0
    ALMOX_INDEX = 1
    ADM_INDEX = 2
    CORTE_INDEX = 3
    ACABAMENTO_INDEX = 4
    TOTAIS_INDEX = 5

    ci = CustoIndireto.objects.all()
    subtotal1 = [0, 0, 0, 0, 0, 0]

    # Custo indireto
    custeio = []
    for idx, custo in enumerate(ci):
        compra = float(custo.porc_compras) * 0.01 * float(custo.valor_mensal)
        subtotal1[COMPRAS_INDEX] += compra
        almoxarifado = float(custo.porc_almoxarifado) * 0.01 * float(custo.valor_mensal)
        subtotal1[ALMOX_INDEX] += almoxarifado
        adm_prod = float(custo.porc_adm_prod) * 0.01 * float(custo.valor_mensal)
        subtotal1[ADM_INDEX] += adm_prod
        corte = float(custo.porc_corte) * 0.01 * float(custo.valor_mensal)
        subtotal1[CORTE_INDEX] += corte
        acabamento = float(custo.porc_acabamento) * 0.01 * float(custo.valor_mensal)
        subtotal1[ACABAMENTO_INDEX] += acabamento
        custeio.append((custo.nome, compra, almoxarifado, adm_prod, corte, acabamento, custo.valor_mensal))
    subtotal1[TOTAIS_INDEX] = sum(subtotal1)

    # Calculo do rateio para o depto de compras
    rateio_compras = [0, 0, 0, 0, 0, 0]
    rateio_compras[COMPRAS_INDEX] = subtotal1[COMPRAS_INDEX]
    rateio_compras[ALMOX_INDEX] = subtotal1[COMPRAS_INDEX] * 0.214285714
    rateio_compras[ADM_INDEX] = subtotal1[COMPRAS_INDEX] * 0.178571429
    rateio_compras[CORTE_INDEX] = subtotal1[COMPRAS_INDEX] * 0.339285714
    rateio_compras[ACABAMENTO_INDEX] = subtotal1[COMPRAS_INDEX] * 0.267857143
    rateio_compras[TOTAIS_INDEX] = 0

    # Subtotal 2
    subtotal2 = [0, 0, 0, 0, 0, 0]
    subtotal2[COMPRAS_INDEX] = 0
    subtotal2[ALMOX_INDEX] = rateio_compras[ALMOX_INDEX] + subtotal1[ALMOX_INDEX]
    subtotal2[ADM_INDEX] = rateio_compras[ADM_INDEX] + subtotal1[ADM_INDEX]
    subtotal2[CORTE_INDEX] = rateio_compras[CORTE_INDEX] + subtotal1[CORTE_INDEX]
    subtotal2[ACABAMENTO_INDEX] = rateio_compras[ACABAMENTO_INDEX] + subtotal1[ACABAMENTO_INDEX]
    subtotal2[TOTAIS_INDEX] = sum(subtotal2)

    # Rateio do depto Almoxarifado
    rateio_almox = [0, 0, 0, 0, 0, 0]
    rateio_almox[COMPRAS_INDEX] = subtotal2[COMPRAS_INDEX]
    rateio_almox[ALMOX_INDEX] = subtotal2[ALMOX_INDEX]
    rateio_almox[ADM_INDEX] = subtotal2[ALMOX_INDEX] * 0.232896652
    rateio_almox[CORTE_INDEX] = subtotal2[ALMOX_INDEX] * 0.347889374
    rateio_almox[ACABAMENTO_INDEX] = subtotal2[ALMOX_INDEX] * 0.419213974
    rateio_almox[TOTAIS_INDEX] = 0

    # Subtotal 3
    subtotal3 = [0, 0, 0, 0, 0, 0]
    subtotal3[COMPRAS_INDEX] = 0
    subtotal3[ALMOX_INDEX] = 0
    subtotal3[ADM_INDEX] = rateio_almox[ADM_INDEX] + subtotal2[ADM_INDEX]
    subtotal3[CORTE_INDEX] = rateio_almox[CORTE_INDEX] + subtotal2[CORTE_INDEX]
    subtotal3[ACABAMENTO_INDEX] = rateio_almox[ACABAMENTO_INDEX] + subtotal2[ACABAMENTO_INDEX]
    subtotal3[TOTAIS_INDEX] = sum(subtotal3)

    # Rateio Adm. da Producao
    rateio_adm = [0, 0, 0, 0, 0, 0]
    rateio_adm[COMPRAS_INDEX] = subtotal3[COMPRAS_INDEX]
    rateio_adm[ALMOX_INDEX] = subtotal3[ALMOX_INDEX]
    rateio_adm[ADM_INDEX] = subtotal3[ADM_INDEX]
    rateio_adm[CORTE_INDEX] = subtotal3[ADM_INDEX] * 0.558926488
    rateio_adm[ACABAMENTO_INDEX] = subtotal3[ADM_INDEX] * 0.441073512
    rateio_adm[TOTAIS_INDEX] = 0

    # Total Depts Prod
    total_depts_prod = [0, 0, 0, 0, 0, 0]
    total_depts_prod[CORTE_INDEX] = subtotal3[CORTE_INDEX] + rateio_adm[CORTE_INDEX]
    total_depts_prod[ACABAMENTO_INDEX] = subtotal3[ACABAMENTO_INDEX] + rateio_adm[ACABAMENTO_INDEX]
    total_depts_prod[TOTAIS_INDEX] = subtotal3[TOTAIS_INDEX]

    # Total de horas produtivas
    horas_prod = [0, 0, 0, 0, 0, 0]
    horas_prod[CORTE_INDEX] = tempo_total_depto('Corte e Costura', 03)
    horas_prod[ACABAMENTO_INDEX] = tempo_total_depto('Acabamento', 03)

    # Custo por hora
    custo_hora = [0, 0, 0, 0, 0, 0]
    custo_hora[CORTE_INDEX] = float(total_depts_prod[CORTE_INDEX]) / float(horas_prod[CORTE_INDEX])
    custo_hora[ACABAMENTO_INDEX] = float(total_depts_prod[ACABAMENTO_INDEX]) / float(horas_prod[ACABAMENTO_INDEX])

    return [custeio, subtotal1, rateio_compras, subtotal2, rateio_almox, subtotal3, rateio_adm, total_depts_prod, horas_prod, custo_hora]


def tempo_total_depto(nome_departamento, num_mes):
    departamento = Departamento.objects.get(nome=nome_departamento)
    tempo_depto = 0
    tempo_depto += tempo_total_produto(departamento, 'Camisetas', num_mes, 2014)
    tempo_depto += tempo_total_produto(departamento, 'Vestidos', num_mes, 2014)
    tempo_depto += tempo_total_produto(departamento, 'Calcas', num_mes, 2014)
    return tempo_depto


def tempo_total_produto(departamento, nome_produto, num_mes, ano):
    produto = Produto.objects.get(nome=nome_produto)
    tempo_produto = TempoProducao.objects.get(departamento=departamento, produto=produto)
    mes = Mes.objects.get(numero=num_mes, ano=ano)
    produto_mes = ProdutoMes.objects.get(produto=produto, mes=mes)
    return tempo_produto.tempo_unitario * produto_mes.producao_mensal
    