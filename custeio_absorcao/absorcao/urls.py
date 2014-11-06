from django.conf.urls import patterns, url
from absorcao import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^produto/$', views.produto_index, name='produto'),
                       url(r'^produto/edit/(?P<id_produto>\w+)/$', views.produto_edit, name='produto_edit'),
                       url(r'^produto/(?P<id_produto>\w+)/$', views.produto_view, name='produto_view'),
                       url(r'^custo-indireto/$', views.custo_indireto_index, name='custo-indireto'),
                       url(r'^custo_indireto/edit/(?P<id_custo_indireto>\w+)/$', views.custo_indireto_edit, name='custo_indireto'),
                       url(r'^despesa/$', views.despesas_index, name='despesas'),
                       url(r'^despesa/edit/(?P<id_despesa>\w+)/$', views.despesa_edit, name='despesa_edit'),
                       url(r'^custo-direto/$', views.custo_direto_index, name='custo_direto'),
                       url(r'^custo-direto/edit/(?P<mes>\w+)/$', views.custo_direto_edit, name='custo_direto_edit'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^tempo-producao/$', views.tempo_producao, name='tempo-producao'),
                       url(r'^tempo-producao/edit/(?P<id_tempo>\w+)/$', views.tempo_producao_edit, name='tempo-producao_edit'),
                       url(r'^relatorio/$', views.relatorio, name='relatorio'),
                       url(r'^relatorio/dre$', views.dre, name='dre'),
                    )
