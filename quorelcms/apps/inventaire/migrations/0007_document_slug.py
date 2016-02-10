# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0006_auto_20160129_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(default='', help_text='indiquer un nom unique pour url', verbose_name='slug', max_length=64),
        ),
    ]
