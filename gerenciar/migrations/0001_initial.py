# Generated by Django 5.1 on 2024-09-02 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('situacao', models.CharField(choices=[('ativa', 'Ativa'), ('inativa', 'Inativa')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario_inicio', models.TimeField()),
                ('horario_termino', models.TimeField()),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciar.sala')),
            ],
        ),
    ]
