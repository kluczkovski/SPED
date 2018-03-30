from .models import *
from django import forms
from input_mask.widgets import InputMask

class DataCustomInput(InputMask):
    mask = {
        'mask': '99/99/9999',
    }

class UnidadeFederacaoForm(forms.ModelForm):
    sigla_UF_IBGE = forms.CharField(
        label="Sigla UF IBGE",
        required=True,
    )
    codigo_UF_IBGE = forms.IntegerField(
        label="Código UF IBGE",
        required=True,
    )
    data_inicio_validade = forms.DateField(
        label="Data Início Validade",
        required=True,
        widget=DataCustomInput(attrs={'class': 'form-control', 'data-mask': '00/00/0000', 'placeholder': 'mm/dd/YYYY'})
    )

    data_fim_validade = forms.DateField(
        required=False,
        widget=DataCustomInput(attrs={'data-mask': '00/00/0000', 'placeholder': 'mm/dd/YYYY'}),
        label="Data Fim Validade")

    class Meta:
        model = UnidadesFederacao
        fields = ['sigla_UF_IBGE', 'codigo_UF_IBGE', 'data_inicio_validade', 'data_fim_validade']

