# -*- coding: utf-8 -*-

import os


def populate():
    dep_corte = add_departamento('Corte e Costura', True)
    dep_acabamento = add_departamento('Acabamento', True)
    add_departamento('Compras', False)
    add_departamento('Almoxarifado', False)
    add_departamento('Adm. Produção', False)

    prod_camisetas = add_produto('Camisetas')
    prod_vestidos = add_produto('Vestidos')
    prod_calcas = add_produto('Calças')

    jan = add_mes('Jan', 1, 2014, 'Janeiro')
    fev = add_mes('Fev', 2, 2014, 'Fevereiro')
    mar = add_mes('Mar', 3, 2014, 'Março')
    abr = add_mes('Abr', 4, 2014, 'Abril')
    mai = add_mes('Mai', 5, 2014, 'Maio')
    jun = add_mes('Jun', 6, 2014, 'Junho')
    jul = add_mes('Jul', 7, 2014, 'Julho')
    ago = add_mes('Ago', 8, 2014, 'Agosto')
    setm = add_mes('Set', 9, 2014, 'Setembro')
    out = add_mes('Out', 10, 2014, 'Outubro')
    nov = add_mes('Nov', 11, 2014, 'Novembro')
    dez = add_mes('Dez', 12, 2014, 'Dezembro')

    meses = (jan, fev, mar, abr, mai, jun, jul, ago, setm, out, nov, dez)

    custo_dir_tecido = add_custo_direto('Tecido')
    custo_dir_aviamentos = add_custo_direto('Aviamentos')
    custo_dir_mod = add_custo_direto('Mão-de-obra Direta')

    for mes in meses:
        add_prod_mes(prod_camisetas, mes, 18000, 18000, 10)
        add_prod_mes(prod_vestidos, mes, 4200, 4200, 22)
        add_prod_mes(prod_calcas, mes, 13000, 13000, 16)

        add_custo_direto_produto(prod_camisetas, custo_dir_tecido, mes, 3.00)
        add_custo_direto_produto(prod_camisetas, custo_dir_aviamentos, mes, 0.25)
        add_custo_direto_produto(prod_camisetas, custo_dir_mod, mes, 0.5)
        add_custo_direto_produto(prod_vestidos, custo_dir_tecido, mes, 4.00)
        add_custo_direto_produto(prod_vestidos, custo_dir_aviamentos, mes, 0.75)
        add_custo_direto_produto(prod_vestidos, custo_dir_mod, mes, 1.00)
        add_custo_direto_produto(prod_calcas, custo_dir_tecido, mes, 3.00)
        add_custo_direto_produto(prod_calcas, custo_dir_aviamentos, mes, 0.50)
        add_custo_direto_produto(prod_calcas, custo_dir_mod, mes, 0.75)

    add_tempo_producao(prod_camisetas, dep_corte, 0.3)
    add_tempo_producao(prod_vestidos, dep_corte, 0.7)
    add_tempo_producao(prod_calcas, dep_corte, 0.8)
    add_tempo_producao(prod_camisetas, dep_acabamento, 0.15)
    add_tempo_producao(prod_vestidos, dep_acabamento, 0.6)
    add_tempo_producao(prod_calcas, dep_acabamento, 0.3)

    add_custo_indireto('Aluguel', 24000, 17.5000000000, 19.1666666667, 17.5000000000, 25.0000000000, 20.8333333333)
    add_custo_indireto('Energia Eletrica', 42000, 15.4761904762, 13.0952380952, 11.9047619048, 33.3333333333, 26.1904761905)
    add_custo_indireto('Salários Pessoal Supervisao', 25000, 15.6000000000, 13.4000000000, 21.0000000000, 28.0000000000, 22.0000000000)
    add_custo_indireto('Mao-de-obra Indireta', 35000, 14.2857142857, 9.7142857143, 19.1428571429, 34.2857142857, 22.5714285714)
    add_custo_indireto('Depreciação', 32000, 12.5000000000, 14.0625000000, 15.3125000000, 29.6875000000, 28.4375000000)
    add_custo_indireto('Materiais de Consumo', 12000, 16.6666666667, 8.3333333333, 15.0000000000, 35.0000000000, 25.0000000000)
    add_custo_indireto('Seguros', 20000, 12.0000000000, 30.0000000000, 10.0000000000, 24.5000000000, 23.5000000000)

    add_despesa('Administrativas', 50000)
    add_despesa('Com Vendas', 43000)
    add_despesa('Comissões (porcentagem das vendas)', 5)

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


def add_mes(abreviacao, numero, ano, nome):
    m = Mes.objects.get_or_create(abreviacao=abreviacao, ano=ano, numero=numero, nome=nome)[0]
    return m


def add_prod_mes(produto, mes, pm, vm, pv):
    pm = ProdutoMes.objects.get_or_create(produto=produto, mes=mes, producao_mensal=pm, vendas_mensal=vm, preco_venda_unitario=pv)
    return pm

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custeio_absorcao.settings')
    from absorcao.models import *
    populate()
