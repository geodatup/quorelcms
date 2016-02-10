from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
import django_tables2 as tables
#import mptt
# import GIS
from django.contrib.gis.db import models as gismodels



# Create your models here.
@python_2_unicode_compatible
class Document(models.Model):
    nom_document = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    annee = models.PositiveIntegerField(validators=[MaxValueValidator(2016)])
    commentaire = models.TextField(blank=True, null=True)
    traitement = models.BooleanField()
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)

    #@permalink
    def get_absolute_url(self):
        return reverse('docDetail', args=[self.pk])

    def __str__(self):
    	return self.nom_document

# try:
#     mptt.register(Document)
# except mptt.AlreadyRegistered:
#     pass

@python_2_unicode_compatible
class Unite(models.Model):
    nom_unite = models.CharField(max_length=100)
    profondeur = models.FloatField(default=0.00)
    epaisseur = models.FloatField(default=0.00)
    texture_choix =  (
    ('aucune','aucune'),
    ('caillouteux','caillouteux'),
    ('graveleux','graveleux'),
    ('sableux','sableux'),
    ('limoneux','limoneux'),
    ('argileux','argileux')
    )
    texture_1 = models.CharField(max_length=50,
        choices=texture_choix,
        default='indéfini'
        )
    texture_2 = models.CharField(max_length=50,
        choices=texture_choix,
        default='indéfini'
        )
    couleur_choix =  (
    ('aucune','aucune'),
    ('blanc','blanc'),
    ('gris','gris'),
    ('noir','noir'),
    ('brun','brun'),
    ('jaune','jaune'),
    ('orange','orange'),
    ('rouge','rouge'),
    ('vert','vert'),
    ('bleu','bleu'),
    ('rouille','rouille')
    )
    couleur = models.CharField(max_length=50,
        choices=couleur_choix,
        default='indéfini'
        )
    nuance_couleur = models.CharField(max_length=50,
        choices=couleur_choix,
        default='indéfini'
        )
    valeur_choix = (
    ('très sombre','très sombre'),
    ('sombre', 'sombre'),
    ('aucune','aucune'),
    ('clair','clair'),
    ('très clair','très clair')
    )
    valeur_couleur = models.CharField(max_length=50,
        choices=valeur_choix,
        default='aucune'
        )
    couleur_MSCC = models.CharField(max_length=100)
    tache = models.TextField(blank=True, null=True)
    carbonate = models.BooleanField()
    type_carbon_choix =(
        ('masse fine','masse fine'),
        ('secondaire','secondaire'),
        ('poupées','poupées'),
        ('pseudo-mycélium','pseudo-mycélium'),
        ('aucune','aucune')
    )
    type_carbon = models.CharField(max_length=50,
        choices=type_carbon_choix,
        default='indéfini'
        )
    structure_choix =  (
    ('massive','massive'),
    ('lamellaire','lamellaire'),
    ('polyédrique','polyédrique'),
    ('prismatique','prismatique'),
    ('grumeleuse','grumeleuse'),
    ('grenue','grenue')
    )
    structure_1 = models.CharField(max_length=50,
        choices=structure_choix,
        default='indéfini'
        )
    taille_structure_choix = (
        ('très fine', 'très fine'),
        ('fine', 'fine'),
        ('pas de taille particulière','pas de taille particulière'),
        ('grossière','grossière'),
        ('très grossière','très grossière')
    )
    taille_structure = models.CharField(max_length=50,
        choices=taille_structure_choix,
        default='pas de taille particulière'
        )
    structure_2 = models.CharField(max_length=50,
        choices=structure_choix,
        default='indéfini'
        )
    sous_structure = models.CharField(max_length=50,
        choices=structure_choix,
        default='indéfini'
        )
    description_structure = models.CharField(blank=True, max_length=100, null=True)
    compacite_choix = (
        ('très compact', 'très compact'),
        ('compact', 'compact'),
        ('peu compact','peu compact'),
        ('meuble','meuble'),
        ('très meuble','très meuble')
    )
    compacite = models.CharField(max_length=50,
        choices=compacite_choix,
        default='indéfini'
        )
    inclusion = models.CharField(blank=True, max_length=100, null=True)
    mobilier = models.TextField(blank=True, null=True)
    perturbation = models.TextField(blank=True, null=True)
    interpretation_sedimentaire = models.CharField(blank=True, max_length=100, null=True)
    interpretation_pedologique = models.CharField(blank=True, max_length=100, null=True)
    interface = models.CharField(max_length=100, null=True)
    echantillon = models.CharField(max_length=100, default='indéfini')
    autre = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_unite


@python_2_unicode_compatible
class Sequence(models.Model):
    nom_sequence = models.CharField(unique=True, max_length=50)
    unite = models.ManyToManyField(Unite)

    def __str__(self):
    	return self.nom_sequence

@python_2_unicode_compatible
class Mention(models.Model):
    mention = models.TextField()
    page = models.CharField(max_length=50)
    commentaire = models.TextField(blank=True, null=True)
    document = models.ForeignKey(Document, blank=True, null=True)
    sequence =  models.ManyToManyField(Sequence)

    def __str__(self):
    	return self.mention

@python_2_unicode_compatible
class Operation(models.Model):
    nom_operation = models.CharField(max_length=100)
    type_op_choix =  (
    ('fouille préventive','fouille préventive'),
    ('diagnostic préventif','diagnostic préventif'),
    ('fouille programmée','fouille programmée'),
    ('carrière','carrière'),
    ('autre chantier','autre chantier'),
    ('autre','autre'),
    )
    type_operation = models.CharField(max_length=25,
    	choices=type_op_choix,
    	default='indéfini'
    	)
    geom = gismodels.PointField(null=True, blank=True, dim=3)
    z = models.FloatField(null=True, blank=True)
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)

    def geom_as_text(self):
        return self.geom

    @property
    def popupContent(self):
      return '<a href="'+ self.slug +'">'+ self.nom_operation +'</a>'

    def __str__(self):
    	return self.nom_operation + ' : ' + self.type_operation



@python_2_unicode_compatible  # only if you need to support Python 2
class Sondage(models.Model):
    nom_sondage = models.CharField(max_length=100)
    operation = models.ForeignKey(Operation, blank=True, null=True)

    geom = gismodels.PointField(null=True, blank=True, dim=3)

    def __str__(self):
    	return self.nom_sondage


@python_2_unicode_compatible
class Observation(models.Model):
    nom_observation = models.CharField(max_length=100)
    type_obs_choix = (
    ('log','log'),
    ('coupe','coupe'),
    ('plan','plan'),
    )
    type_observation = models.CharField(max_length=50,
    	choices=type_obs_choix,
    	default='indéfini'
    	)
    sondage = models.ForeignKey(Sondage, blank=True, null=True)
    sequence = models.ForeignKey(Sequence, blank=True, null=True)

    acces_possible = models.BooleanField()


    def __str__(self):
    	return self.nom_observation



class UniteTableFull(tables.Table):
    unite = tables.Column(accessor='nom_unite')
    #title = tables.Column()
    epaisseur = tables.Column(accessor='epaisseur')
    texture_1 = tables.Column(verbose_name="texture_1")
    texture_2 = tables.Column(verbose_name="texture_2")
     
    class Meta:
        model = Unite
        exclude = ()
        attrs = {"class": "paleblue"}



