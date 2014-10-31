from django.contrib.auth.models import User
from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=128)
    producao = models.BooleanField()

    def __unicode__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=128)

    def __unicode__(self):
        return self.nome


class Mes(models.Model):
    abreviacao = models.CharField(max_length=5)
    ano = models.IntegerField()
    numero = models.IntegerField()

    def __unicode__(self):
        return self.abreviacao


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username
        

class ProdutoMes(models.Model):
    produto = models.ForeignKey(Produto)
    mes = models.ForeignKey(Mes)
    producao_mensal = models.IntegerField()
    preco_venda_unitario = models.DecimalField(decimal_places=2, max_digits=10)

    def __unicode__(self):
        return str(self.produto) + ' - ' + str(self.mes)


class TempoProducao(models.Model):
    produto = models.ForeignKey(Produto)
    departamento = models.ForeignKey(Departamento)
    tempo_unitario = models.DecimalField(decimal_places=2, max_digits=5)

    def __unicode__(self):
        return str(self.produto) + ' - ' + str(self.departamento) + ' - ' + str(self.tempo_unitario)


class CustoDireto(models.Model):
    nome = models.CharField(max_length=128)

    def __unicode__(self):
        return self.nome


class CustoDiretoProduto(models.Model):
    produto = models.ForeignKey(Produto)
    custo_direto = models.ForeignKey(CustoDireto)
    mes = models.ForeignKey(Mes)
    valor_unitario = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __unicode__(self):
        return str(self.produto) + ' - ' + str(self.valor_unitario)


class CustoIndireto(models.Model):
    nome = models.CharField(max_length=128)
    valor_mensal = models.DecimalField(decimal_places=2, max_digits=10)

    def __unicode__(self):
        return self.nome


class Despesa(models.Model):
    nome = models.CharField(max_length=128)
    valor_mensal = models.DecimalField(decimal_places=2, max_digits=10)

    def __unicode__(self):
        return self.nome
