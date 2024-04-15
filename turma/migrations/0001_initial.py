# Generated by Django 5.0.1 on 2024-04-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_turma', models.CharField(max_length=50)),
                ('data_criacao', models.DateTimeField(default='1999-01-01')),
            ],
            options={
                'verbose_name': 'Turma',
            },
        ),
    ]
