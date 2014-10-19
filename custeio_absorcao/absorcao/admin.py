from django.contrib import admin
from absorcao.models import Departamento, TempoProducao, CustoDireto, CustoDiretoProduto, CustoIndireto, Despesa

admin.site.register(Departamento)
admin.site.register(TempoProducao)
admin.site.register(CustoDireto)
admin.site.register(CustoDiretoProduto)
admin.site.register(CustoIndireto)
admin.site.register(Despesa)
