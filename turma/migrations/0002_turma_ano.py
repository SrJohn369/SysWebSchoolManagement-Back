# Generated by Django 5.0.1 on 2024-04-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='ano',
            field=models.CharField(default='1ª Ano', max_length=10),
        ),
    ]
