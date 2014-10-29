# -*- coding: utf-8 -*-

import os


def populate():
    dep_corte = add_departamento('Corte e Costura', True)
    dep_acabamento = add_departamento('Acabamento', True)
    dep_compras = add_departamento('Compras', False)
    dep_almox = add_departamento('Almoxarifado', False)
    dep_adm = add_departamento('Adm. Producao', False)

    prod_camisetas = add_produto('Camisetas', 18000, 10)
    prod_vestidos = add_produto('Vestidos', 4200, 22)
    prod_calcas = add_produto('Calcas', 13000, 16)

    add_tempo_producao(prod_camisetas, dep_corte, 0.3)
    add_tempo_producao(prod_vestidos, dep_corte, 0.7)
    add_tempo_producao(prod_calcas, dep_corte, 0.8)
    add_tempo_producao(prod_camisetas, dep_acabamento, 0.15)
    add_tempo_producao(prod_vestidos, dep_acabamento, 0.6)
    add_tempo_producao(prod_calcas, dep_acabamento, 0.3)

    custo_dir_tecido = add_custo_direto('Tecido')
    custo_dir_aviamentos = add_custo_direto('Aviamentos')
    custo_dir_mod = add_custo_direto('Mao-de-obra Direta')

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, 3.00)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, 0.25)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, 0.5)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, 4.00)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, 0.75)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, 1.00)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, 3.00)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, 0.50)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, 0.75)

    add_custo_indireto('Alguel', 24000)
    add_custo_indireto('Energia Eletrica', 42000)
    add_custo_indireto('Salários Pessoal Supervisao', 25000)
    add_custo_indireto('Mao-de-obra Indireta', 35000)
    add_custo_indireto('Depreciacao', 32000)
    add_custo_indireto('Materiais de Consumo', 12000)
    add_custo_indireto('Seguros', 20000)

    add_despesa('Administrativas', 50000)
    add_despesa('Com Vendas', 43000)
    add_despesa('Comissoes (5 por cento das Vendas)', 43000)

    # Print out what we have added to the user.
#    for c in Departamento.objects.all():
 #      for p in Page.objects.filter(category=c):
  #        print "- {0} - {1}".format(str(c), str(p))


def add_produto(nome, pm, pv):
    p = Produto.objects.get_or_create(nome=nome, producao_mensal=pm, preco_venda_unitario=pv)[0]
    return p


def add_departamento(nome, producao):
    d = Departamento.objects.get_or_create(nome=nome, producao=producao)[0]
    return d


def add_tempo_producao(produto, departamento, tempo):
    t = TempoProducao.objects.get_or_create(produto=produto, departamento=departamento, tempo_unitario=tempo)[0]
    return t


def add_custo_direto(nome):
    cd = CustoDireto.objects.get_or_create(nome=nome)[0]
    return cd


def add_custo_direto_produto(produto, custo_direto, valor_unitario):
    cdp = CustoDiretoProduto.objects.get_or_create(produto=produto, custo_direto=custo_direto, valor_unitario=valor_unitario)[0]
    return cdp


def add_custo_indireto(nome, valor_mensal):
    ci = CustoIndireto.objects.get_or_create(nome=nome, valor_mensal=valor_mensal)[0]
    return ci


def add_despesa(nome, valor_mensal):
    d = Despesa.objects.get_or_create(nome=nome, valor_mensal=valor_mensal)[0]
    return d

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custeio_absorcao.settings')
    from absorcao.models import *
    populate()
