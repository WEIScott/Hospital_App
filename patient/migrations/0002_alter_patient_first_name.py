# Generated by Django 3.2.8 on 2021-11-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Patient`s First Name'),
        ),
    ]
