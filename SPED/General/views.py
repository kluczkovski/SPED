from django.shortcuts import render, redirect, get_object_or_404
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


def unidadeFederacao_edit(request, uf_id, template_name='UnidadeFederacao/uf_form.html'):
    uf = get_object_or_404(UnidadesFederacao, pk=uf_id)
    if request.method == "POST":
        form = UnidadeFederacaoForm(request.POST, instance=uf)
        if form.is_valid():
            form.save()
            return redirect('uf_list')
    else:
        form = UnidadeFederacaoForm(instance=uf)

    return render(request, template_name, {'form': form})


def unidadeFederacao_delete(request, uf_id, template_name='UnidadeFederacao/uf_delete.html'):
    uf = get_object_or_404(UnidadesFederacao, pk=uf_id)
    if request.method == "POST":
        uf.delete()
        return redirect('uf_list')
    return render(request, template_name, {'uf': uf})

