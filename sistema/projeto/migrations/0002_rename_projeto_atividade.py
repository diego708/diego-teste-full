# Generated by Django 5.0.6 on 2024-05-25 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projeto',
            new_name='Atividade',
        ),
    ]
