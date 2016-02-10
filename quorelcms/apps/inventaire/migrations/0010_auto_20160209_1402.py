# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0009_operation_z'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unite',
            name='echantillon',
            field=models.CharField(max_length=100, default='indéfini'),
        ),
    ]
