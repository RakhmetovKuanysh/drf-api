# Generated by Django 2.0.3 on 2018-04-06 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20180406_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]