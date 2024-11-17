from django.contrib import admin
from django.urls import path
from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:id>/', views.cliente_update, name='cliente_update'),
]
