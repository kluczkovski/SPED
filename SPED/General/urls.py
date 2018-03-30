from django.urls import path
from . import views

urlpatterns = [
    path('UnidadeFederacao/list', views.unidadeFederacao_list, name='uf_list'),
    path('UnidadeFederacao/create', views.unidadeFederacao_create, name='uf_create'),
]
