# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0007_document_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='slug',
            field=models.SlugField(help_text='indiquer un nom unique pour url', default='', verbose_name='slug', max_length=64),
        ),
    ]
