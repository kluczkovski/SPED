# Generated by Django 2.0.3 on 2018-03-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadesfederacao',
            name='codigo_UF_IBGE',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]