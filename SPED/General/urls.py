from django.urls import path
from . import views

urlpatterns = [
    path('UnidadeFederecao/list', views.UnidadeFederacao_list, name='General/Unidade Federação/List')
]
