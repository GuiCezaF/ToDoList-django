# Generated by Django 5.0.6 on 2024-05-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    
    # TODO(guilherme): Fazer uma seed só para deixar de exemplo

    def seed_func():
        pass
    
    def reverse_func():
        pass

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome da Tarefa')),
                ('description', models.TextField(verbose_name='Descrição da tarefa')),
                ('status', models.BooleanField(verbose_name='Status da tarefa')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Data de atualização')),
            ],
        ),
        migrations.RunPython(seed_func, reverse_func),
    ]
