# Generated by Django 2.0.3 on 2018-03-23 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0002_auto_20180323_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidadesfederacao',
            name='data_ultima_atualizacao',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 23, 12, 30, 31, 475024)),
        ),
    ]
