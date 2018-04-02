from django.urls import path
from . import views

urlpatterns = [
    path('UnidadeFederacao/list', views.unidadeFederacao_list, name='uf_list'),
    path('UnidadeFederacao/create', views.unidadeFederacao_create, name='uf_create'),
    path('UnidadeFederacao/edit/<int:uf_id>', views.unidadeFederacao_edit, name='uf_edit'),
    path('UnidadeFederacao/delete/<int:uf_id>', views.unidadeFederacao_delete, name='uf_delete')
]
