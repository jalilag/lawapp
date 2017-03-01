# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-27 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Intervenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_type', models.IntegerField(choices=[(1, 'Personne physique'), (2, 'Personne morale')], default=1)),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='dossier',
            name='adversaire',
            field=models.ManyToManyField(related_name='adversaire', to='dossier.Intervenant'),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client',
            field=models.ManyToManyField(related_name='client', to='dossier.Intervenant'),
        ),
    ]
