# Generated by Django 3.2.9 on 2021-12-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('insurancecompany_id', models.IntegerField(primary_key=True, serialize=False)),
                ('insurancecompany_name', models.CharField(max_length=500)),
                ('company_detail', models.TextField()),
            ],
        ),
    ]
