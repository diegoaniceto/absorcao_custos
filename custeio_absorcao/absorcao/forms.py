from django import forms
from absorcao.models import Produto, Despesa, CustoIndireto


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(max_length=128, help_text="Nome do produto")
    producao_mensal = forms.IntegerField()
    preco_venda_unitario = forms.DecimalField(decimal_places=2)

    class Meta:
        model = Produto

class DespesaForm(forms.ModelForm):
    nome = forms.CharField(max_length=128)
    valor_mensal = forms.DecimalField(decimal_places=2)

    class Meta:
        model = Despesa

class CustoIndiretoForm(forms.ModelForm):
    nome = forms.CharField(max_length=128)
    valor_mensal = forms.DecimalField(decimal_places=2)

    class Meta:
        model = CustoIndireto