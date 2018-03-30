from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

# Unidades Federação - Siglas
def unidadeFederacao_list(request, template_name='UnidadeFederacao/uf_list.html'):
    query = request.GET.get("UFsearch")
    if query:
        ufs = UnidadesFederacao.objects.filter(sigla_UF_IBGE__icontains=query)
    else:
        ufs = UnidadesFederacao.objects.all()
    return render(request, template_name, {'ufs': ufs})


def unidadeFederacao_create(request, template_name='UnidadeFederacao/uf_form.html'):
     form = UnidadeFederacaoForm(request.POST or None)
     if form.is_valid():
         form.save()
         return redirect('uf_list')

     return render(request, template_name, {'form': form})
