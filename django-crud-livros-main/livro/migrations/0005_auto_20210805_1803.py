# Generated by Django 3.2.6 on 2021-08-05 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livro", "0004_alter_livros_data_cadastro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livros",
            name="data_cadastro",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name="livros",
            name="data_devolucao",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="livros",
            name="data_emprestimo",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="livros",
            name="nome_emprestado",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="livros",
            name="tempo_duracao",
            field=models.DateField(blank=True, null=True),
        ),
    ]
