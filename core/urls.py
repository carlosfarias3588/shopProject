from django.contrib import admin
from django.urls import path
from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:id>/', views.cliente_update, name='cliente_update'),

    path('produto/', views.produto_list, name='produto_list'),
    path('produto/novo/', views.produto_create, name='produto_create'),
    path('produto/<int:id>/', views.produto_update, name='produto_update'),

    path('venda/', views.venda_list, name='venda_list'),
    path('venda/novo/', views.venda_create, name='venda_create'),
    path('venda/<int:id>/', views.venda_update, name='venda_update'),


]
