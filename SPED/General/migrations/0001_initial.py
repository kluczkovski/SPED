# Generated by Django 2.0.3 on 2018-03-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadesFederacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_UF_IBGE', models.PositiveIntegerField(max_length=5, unique=True)),
                ('sigla_UF_IBGE', models.CharField(max_length=2, unique=True)),
                ('data_inicio_validade', models.DateField(null=True)),
                ('data_fim_validade', models.DateField(null=True)),
            ],
        ),
    ]
