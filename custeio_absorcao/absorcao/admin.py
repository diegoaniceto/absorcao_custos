from django.contrib import admin
from absorcao.models import Departamento, TempoProducao, CustoDireto, CustoDiretoProduto, CustoIndireto, Despesa, Produto, ProdutoMes, Mes

admin.site.register(Departamento)
admin.site.register(Produto)
admin.site.register(ProdutoMes)
admin.site.register(Mes)
admin.site.register(TempoProducao)
admin.site.register(CustoDireto)
admin.site.register(CustoDiretoProduto)
admin.site.register(CustoIndireto)
admin.site.register(Despesa)
