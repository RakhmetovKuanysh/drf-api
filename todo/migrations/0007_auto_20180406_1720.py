# Generated by Django 2.0.3 on 2018-04-06 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20180406_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 6, 17, 20, 25, 885530)),
        ),
    ]
