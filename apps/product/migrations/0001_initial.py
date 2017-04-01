# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 21:44
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from=('name',), unique=True, verbose_name='slug')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8, verbose_name='Preço')),
                ('description', models.TextField(verbose_name='Conteudo')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]