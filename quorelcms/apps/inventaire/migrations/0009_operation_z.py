# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0008_operation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='z',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
