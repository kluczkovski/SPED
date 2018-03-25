from django.shortcuts import render
from .models import *

# Create your views here.

def UnidadeFederacao_list(request, template_name='UnidadeFederecao/list.html'):
    ufs = UnidadesFederacao.objects.all()
    return render(request, template_name, {'ufs': ufs})