# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_doc', models.CharField(default='indéfini', choices=[('Notice explicative de la carte pédologique de la France', 'Notice explicative de la carte pédologique de la France'), ('Notice explicative de la carte géomorphologique détaillée de la France', 'Notice explicative de la carte géomorphologique détaillée de la France'), ('Recherches archéologiques préventives', 'Recherches archéologiques préventives'), ('Rapport de diagnostique archéologique', 'Rapport de diagnostique archéologique'), ('Autre', 'Autre')], max_length=300)),
                ('nom_document', models.CharField(max_length=300)),
                ('auteur', models.CharField(max_length=100)),
                ('annee', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2016)])),
                ('commentaire', models.TextField(null=True, blank=True)),
                ('traitement', models.BooleanField()),
                ('slug', models.SlugField(default='', verbose_name='slug', help_text='indiquer un nom unique pour url', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Mention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mention', models.TextField()),
                ('page', models.CharField(max_length=50)),
                ('commentaire', models.TextField(null=True, blank=True)),
                ('document', models.ForeignKey(null=True, to='inventaire.Document', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_observation', models.CharField(max_length=100)),
                ('type_observation', models.CharField(default='indéfini', choices=[('log', 'log'), ('coupe', 'coupe'), ('plan', 'plan')], max_length=50)),
                ('acces_possible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_operation', models.CharField(max_length=100)),
                ('type_operation', models.CharField(default='indéfini', choices=[('fouille préventive', 'fouille préventive'), ('diagnostic préventif', 'diagnostic préventif'), ('fouille programmée', 'fouille programmée'), ('carrière', 'carrière'), ('autre chantier', 'autre chantier'), ('autre', 'autre')], max_length=25)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, dim=3, srid=4326, blank=True)),
                ('z', models.FloatField(null=True, blank=True)),
                ('slug', models.SlugField(default='', verbose_name='slug', help_text='indiquer un nom unique pour url', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_sequence', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sondage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_sondage', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, dim=3, srid=4326, blank=True)),
                ('operation', models.ForeignKey(null=True, to='inventaire.Operation', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_unite', models.CharField(max_length=100)),
                ('profondeur', models.FloatField(default=0.0)),
                ('epaisseur', models.FloatField(default=0.0)),
                ('texture_1', models.CharField(default='indéfini', choices=[('aucune', 'aucune'), ('caillouteux', 'caillouteux'), ('graveleux', 'graveleux'), ('sableux', 'sableux'), ('limoneux', 'limoneux'), ('argileux', 'argileux')], max_length=50)),
                ('texture_2', models.CharField(default='indéfini', choices=[('aucune', 'aucune'), ('caillouteux', 'caillouteux'), ('graveleux', 'graveleux'), ('sableux', 'sableux'), ('limoneux', 'limoneux'), ('argileux', 'argileux')], max_length=50)),
                ('couleur', models.CharField(default='indéfini', choices=[('aucune', 'aucune'), ('blanc', 'blanc'), ('gris', 'gris'), ('noir', 'noir'), ('brun', 'brun'), ('jaune', 'jaune'), ('orange', 'orange'), ('rouge', 'rouge'), ('vert', 'vert'), ('bleu', 'bleu'), ('rouille', 'rouille')], max_length=50)),
                ('nuance_couleur', models.CharField(default='indéfini', choices=[('aucune', 'aucune'), ('blanc', 'blanc'), ('gris', 'gris'), ('noir', 'noir'), ('brun', 'brun'), ('jaune', 'jaune'), ('orange', 'orange'), ('rouge', 'rouge'), ('vert', 'vert'), ('bleu', 'bleu'), ('rouille', 'rouille')], max_length=50)),
                ('valeur_couleur', models.CharField(default='aucune', choices=[('très sombre', 'très sombre'), ('sombre', 'sombre'), ('aucune', 'aucune'), ('clair', 'clair'), ('très clair', 'très clair')], max_length=50)),
                ('couleur_MSCC', models.CharField(max_length=100)),
                ('tache', models.TextField(null=True, blank=True)),
                ('carbonate', models.BooleanField()),
                ('type_carbon', models.CharField(default='indéfini', choices=[('masse fine', 'masse fine'), ('secondaire', 'secondaire'), ('poupées', 'poupées'), ('pseudo-mycélium', 'pseudo-mycélium'), ('aucune', 'aucune')], max_length=50)),
                ('structure_1', models.CharField(default='indéfini', choices=[('massive', 'massive'), ('lamellaire', 'lamellaire'), ('polyédrique', 'polyédrique'), ('prismatique', 'prismatique'), ('grumeleuse', 'grumeleuse'), ('grenue', 'grenue')], max_length=50)),
                ('taille_structure', models.CharField(default='pas de taille particulière', choices=[('très fine', 'très fine'), ('fine', 'fine'), ('pas de taille particulière', 'pas de taille particulière'), ('grossière', 'grossière'), ('très grossière', 'très grossière')], max_length=50)),
                ('structure_2', models.CharField(default='indéfini', choices=[('massive', 'massive'), ('lamellaire', 'lamellaire'), ('polyédrique', 'polyédrique'), ('prismatique', 'prismatique'), ('grumeleuse', 'grumeleuse'), ('grenue', 'grenue')], max_length=50)),
                ('sous_structure', models.CharField(default='indéfini', choices=[('massive', 'massive'), ('lamellaire', 'lamellaire'), ('polyédrique', 'polyédrique'), ('prismatique', 'prismatique'), ('grumeleuse', 'grumeleuse'), ('grenue', 'grenue')], max_length=50)),
                ('description_structure', models.CharField(null=True, max_length=100, blank=True)),
                ('compacite', models.CharField(default='indéfini', choices=[('très compact', 'très compact'), ('compact', 'compact'), ('peu compact', 'peu compact'), ('meuble', 'meuble'), ('très meuble', 'très meuble')], max_length=50)),
                ('inclusion', models.CharField(null=True, max_length=100, blank=True)),
                ('mobilier', models.TextField(null=True, blank=True)),
                ('perturbation', models.TextField(null=True, blank=True)),
                ('interpretation_sedimentaire', models.CharField(null=True, max_length=100, blank=True)),
                ('interpretation_pedologique', models.CharField(null=True, max_length=100, blank=True)),
                ('interface', models.CharField(null=True, max_length=100)),
                ('echantillon', models.CharField(default='indéfini', max_length=100)),
                ('autre', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='sequence',
            name='unite',
            field=models.ManyToManyField(to='inventaire.Unite'),
        ),
        migrations.AddField(
            model_name='observation',
            name='sequence',
            field=models.ForeignKey(null=True, to='inventaire.Sequence', blank=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='sondage',
            field=models.ForeignKey(null=True, to='inventaire.Sondage', blank=True),
        ),
        migrations.AddField(
            model_name='mention',
            name='sequence',
            field=models.ManyToManyField(to='inventaire.Sequence'),
        ),
    ]
