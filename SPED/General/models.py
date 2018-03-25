from django.utils import timezone
from django.db import models

class UnidadesFederacao(models.Model):

    # DataBase fields
    codigo_UF_IBGE = models.PositiveIntegerField(null=False, unique=True)
    sigla_UF_IBGE = models.CharField(max_length=2, null=False, unique=True)
    data_inicio_validade = models.DateField(null=True)
    data_fim_validade = models.DateField(null=True)
    data_ultima_atualizacao = models.DateTimeField(default=timezone.now)


    # To String method
    def __str__(self):
        return self.sigla_UF_IBGE

    # Save method
    def save(self, *args, **kwargs):
        #validation()
        super().save()

    def importSPED_table(self, line):
        self.save()


'''
class Empresa(models.Model):
    nome_empresarial = models.CharField(max_length=70, null=False)
    CNPJ = models.PositiveIntegerField(max_length=14, null=False, unique=True)

'''
