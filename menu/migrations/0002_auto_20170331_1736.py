# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Right_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Member', verbose_name='Membre')),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='right_job',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Job', verbose_name='Fonction'),
        ),
        migrations.AlterField(
            model_name='right_job',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='right_job',
            name='value',
            field=models.IntegerField(choices=[(0, 'Accès interdit'), (1, 'Accès autorisé')], default=0, verbose_name='Droits'),
        ),
        migrations.AddField(
            model_name='right_member',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu', verbose_name='Menu'),
        ),
    ]