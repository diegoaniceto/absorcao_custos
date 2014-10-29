from django import forms
from absorcao.models import Produto


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(max_length=128, help_text="Nome do produto")
    producao_mensal = forms.IntegerField()
    preco_venda_unitario = forms.DecimalField(decimal_places=2)

    class Meta:
        model = Produto
