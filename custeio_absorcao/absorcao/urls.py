from django.conf.urls import patterns, url
from absorcao import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^produto/$', views.produtoIndex, name='produto'),)
