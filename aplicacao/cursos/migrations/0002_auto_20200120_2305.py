# Generated by Django 2.2.6 on 2020-01-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='descricao',
            field=models.CharField(max_length=500),
        ),
    ]
