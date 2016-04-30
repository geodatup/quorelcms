# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0010_auto_20160209_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type_doc',
            field=models.CharField(max_length=300, default='indéfini', choices=[('Notice explicative de la carte pédologique de la France', 'Notice explicative de la carte pédologique de la France'), ('Notice explicative de la carte géomorphologique détaillée de la France', 'Notice explicative de la carte géomorphologique détaillée de la France'), ('Recherches archéologiques préventives', 'Recherches archéologiques préventives'), ('Rapport de diagnostique archéologique', 'Rapport de diagnostique archéologique'), ('Autre', 'Autre')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='nom_document',
            field=models.CharField(max_length=300),
        ),
    ]
