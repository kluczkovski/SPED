from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class UnidadesFederacao(models.Model):

    # DataBase fields
    codigo_UF_IBGE = models.PositiveIntegerField(null=False, unique=True)
    sigla_UF_IBGE = models.CharField(max_length=2, null=False, unique=True)
    data_inicio_validade = models.DateField(null=True)
    data_fim_validade = models.DateField(null=True, blank=True)
    data_ultima_atualizacao = models.DateTimeField(default=timezone.now)

    # To String method
    def __str__(self):
        return '{} - {} '.format(
            self.sigla_UF_IBGE, self.codigo_UF_IBGE
        )

    # Validation before save
    def clean(self):
        # Data Início não pode ser maior que data fim
        if self.data_fim_validade is not None:
            if self.data_inicio_validade > self.data_fim_validade:
                raise ValidationError(_
                                      ("Data Início %(datainicio)s não pode ser maior que Data Fim %(datafim)s"),
                                      params={'datainicio': self.data_inicio_validade, 'datafim': self.data_fim_validade},
                                      )

    def importSPED_table(self, line):
        self.save()


'''
class Empresa(models.Model):
    nome_empresarial = models.CharField(max_length=70, null=False)
    CNPJ = models.PositiveIntegerField(max_length=14, null=False, unique=True)

'''
