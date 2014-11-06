from absorcao.models import Produto, TempoProducao, Departamento
from django.contrib.auth.models import User
from django import forms
from absorcao.models import Despesa, CustoIndireto
from absorcao.models import ProdutoMes


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(max_length=128)

    class Meta:
        model = Produto


class ProdutoMesForm(forms.ModelForm):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all())
    producao_mensal = forms.IntegerField()
    preco_venda_unitario = forms.DecimalField(decimal_places=2)

    class Meta:
        model = ProdutoMes


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


class TempoProducaoForm(forms.ModelForm):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all())
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all())
    tempo_unitario = forms.DecimalField(decimal_places=2, max_digits=7, required=True)

    class Meta:
        model = TempoProducao


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Senha")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
