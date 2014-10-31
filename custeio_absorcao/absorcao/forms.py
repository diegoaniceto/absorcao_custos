from absorcao.models import PerfilUsuario, Produto
from django.contrib.auth.models import User
from django import forms


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(max_length=128, help_text="Nome do produto")
    producao_mensal = forms.IntegerField()
    preco_venda_unitario = forms.DecimalField(decimal_places=2)

    class Meta:
        model = Produto

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
