# -*- coding: utf-8 -*-

import os


def populate():
    dep_corte = add_departamento('Corte e Costura', True)
    dep_acabamento = add_departamento('Acabamento', True)
    dep_compras = add_departamento('Compras', False)
    dep_almox = add_departamento('Almoxarifado', False)
    dep_adm = add_departamento('Adm. Producao', False)

    prod_camisetas = add_produto('Camisetas')
    prod_vestidos = add_produto('Vestidos')
    prod_calcas = add_produto('Calcas')

    jan = add_mes('Jan', 1, 2014)
    fev = add_mes('Fev', 2, 2014)
    mar = add_mes('Mar', 3, 2014)
    abr = add_mes('Abr', 4, 2014)
    mai = add_mes('Mai', 5, 2014)
    jun = add_mes('Jun', 6, 2014)
    jul = add_mes('Jul', 7, 2014)
    ago = add_mes('Ago', 8, 2014)
    setm = add_mes('Set', 9, 2014)
    out = add_mes('Out', 10, 2014)
    nov = add_mes('Nov', 11, 2014)
    dez = add_mes('Dez', 12, 2014)

    add_prod_mes(prod_camisetas, mar, 18000, 10)
    add_prod_mes(prod_vestidos, mar, 4200, 22)
    add_prod_mes(prod_calcas, mar, 13000, 16)

    add_tempo_producao(prod_camisetas, dep_corte, 0.3)
    add_tempo_producao(prod_vestidos, dep_corte, 0.7)
    add_tempo_producao(prod_calcas, dep_corte, 0.8)
    add_tempo_producao(prod_camisetas, dep_acabamento, 0.15)
    add_tempo_producao(prod_vestidos, dep_acabamento, 0.6)
    add_tempo_producao(prod_calcas, dep_acabamento, 0.3)

    custo_dir_tecido = add_custo_direto('Tecido')
    custo_dir_aviamentos = add_custo_direto('Aviamentos')
    custo_dir_mod = add_custo_direto('Mao-de-obra Direta')

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, mar, 3.00)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, mar, 0.25)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, mar, 0.5)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, mar, 4.00)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, mar, 0.75)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, mar, 1.00)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, mar, 3.00)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, mar, 0.50)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, mar, 0.75)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, jan, 5.00)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, jan, 6.25)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, jan, 2.5)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, jan, 7.00)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, jan, 1.75)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, jan, 2.40)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, jan, 3.50)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, jan, 0.80)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, jan, 2.95)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, fev, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, fev, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, fev, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, fev, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, fev, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, fev, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, fev, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, fev, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, fev, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, abr, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, abr, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, abr, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, abr, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, abr, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, abr, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, abr, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, abr, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, abr, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, mai, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, mai, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, mai, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, mai, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, mai, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, mai, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, mai, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, mai, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, mai, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, jun, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, jun, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, jun, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, jun, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, jun, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, jun, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, jun, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, jun, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, jun, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, jul, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, jul, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, jul, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, jul, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, jul, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, jul, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, jul, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, jul, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, jul, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, ago, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, ago, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, ago, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, ago, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, ago, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, ago, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, ago, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, ago, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, ago, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, setm, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, setm, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, setm, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, setm, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, setm, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, setm, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, setm, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, setm, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, setm, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, out, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, out, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, out, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, out, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, out, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, out, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, out, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, out, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, out, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, nov, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, nov, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, nov, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, nov, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, nov, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, nov, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, nov, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, nov, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, nov, 0)

    add_custo_direto_produto(prod_camisetas, custo_dir_tecido, dez, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, dez, 0)
    add_custo_direto_produto(prod_camisetas, custo_dir_mod, dez, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_tecido, dez, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, dez, 0)
    add_custo_direto_produto(prod_vestidos, custo_dir_mod, dez, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_tecido, dez, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, dez, 0)
    add_custo_direto_produto(prod_calcas, custo_dir_mod, dez, 0)

    add_custo_indireto('Alguel', 24000, 17.50, 19.17, 17.50, 25.00, 20.83)
    add_custo_indireto('Energia Eletrica', 42000, 15.48, 13.10, 11.90, 33.33, 26.19)
    add_custo_indireto('Salários Pessoal Supervisao', 25000, 15.60, 13.40, 21.00, 28.00, 22.00)
    add_custo_indireto('Mao-de-obra Indireta', 35000, 14.29, 9.71, 19.14, 34.29, 22.57)
    add_custo_indireto('Depreciacao', 32000, 12.50, 14.06, 15.31, 29.69, 28.44)
    add_custo_indireto('Materiais de Consumo', 12000, 16.67, 8.33, 15.00, 35.00, 24)
    add_custo_indireto('Seguros', 20000, 12.00, 30.00, 10.00, 24.50, 23.50)

    add_despesa('Administrativas', 50000)
    add_despesa('Com Vendas', 43000)
    add_despesa('Comissoes (5 por cento das Vendas)', 43000)

    # Print out what we have added to the user.
#    for c in Departamento.objects.all():
 #      for p in Page.objects.filter(category=c):
  #        print "- {0} - {1}".format(str(c), str(p))


def add_produto(nome):
    p = Produto.objects.get_or_create(nome=nome)[0]
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


def add_custo_direto_produto(produto, custo_direto, mes, valor_unitario):
    cdp = CustoDiretoProduto.objects.get_or_create(produto=produto, custo_direto=custo_direto, mes=mes, valor_unitario=valor_unitario)[0]
    return cdp


def add_custo_indireto(nome, valor_mensal, porc_compras, porc_almoxarifado, porc_adm_prod, porc_corte, porc_acabamento):
    ci = CustoIndireto.objects.get_or_create(nome=nome, valor_mensal=valor_mensal, porc_compras=porc_compras, porc_almoxarifado=porc_almoxarifado, porc_adm_prod=porc_adm_prod, porc_corte=porc_corte, porc_acabamento=porc_acabamento)[0]
    return ci


def add_despesa(nome, valor_mensal):
    d = Despesa.objects.get_or_create(nome=nome, valor_mensal=valor_mensal)[0]
    return d


def add_mes(abreviacao, numero, ano):
    m = Mes.objects.get_or_create(abreviacao=abreviacao, ano=ano, numero=numero)[0]
    return m


def add_prod_mes(produto, mes, pm, pv):
    pm = ProdutoMes.objects.get_or_create(produto=produto, mes=mes, producao_mensal=pm, preco_venda_unitario=pv)
    return pm

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custeio_absorcao.settings')
    from absorcao.models import *
    populate()
