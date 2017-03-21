# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-17 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('url', models.CharField(blank=True, max_length=50, null=True, verbose_name='Adresse')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu', verbose_name='Parents')),
            ],
        ),
        migrations.CreateModel(
            name='Right_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 'Accès autorisé'), (2, 'Non défini'), (3, 'Accès interdit')], default=2)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Job')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
            ],
        ),
    ]
