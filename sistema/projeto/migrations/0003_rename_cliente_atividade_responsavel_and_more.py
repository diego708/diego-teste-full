# Generated by Django 5.0.6 on 2024-05-25 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
        ('projeto', '0002_rename_projeto_atividade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividade',
            old_name='cliente',
            new_name='responsavel',
        ),
        migrations.AddField(
            model_name='atividade',
            name='projeto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro.projeto'),
            preserve_default=False,
        ),
    ]