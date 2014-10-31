from django.conf.urls import patterns, url
from absorcao import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^produto/$', views.produto_index, name='produto'),
                       url(r'^produto/edit/(?P<id_produto>\w+)/$', views.produto_edit, name='produto_edit'),
                       url(r'^produto/(?P<id_produto>\w+)/$', views.produto_view, name='produto_view'),
                       url(r'^custo_direto/$', views.custo_direto_index, name='custo_direto'),
                       url(r'^custo_direto/edit/(?P<mes>\w+)/$', views.custo_direto_edit, name='custo_direto_edit'),
                       )
