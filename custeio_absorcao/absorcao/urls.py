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
                       url(r'^despesa/edit/(?P<id_despesa>\w+)/$', views.despesa_edit, name='despesa_edit')
                    )
