# Generated by Django 2.0.3 on 2018-03-23 21:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0003_unidadesfederacao_data_ultima_atualizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadesfederacao',
            name='data_ultima_atualizacao',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 23, 21, 3, 42, 194258, tzinfo=utc)),
        ),
    ]