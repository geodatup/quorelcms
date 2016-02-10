from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from django import forms


# Register your models here.
from .models import Document, Mention, Observation, Sondage, Operation, Sequence, Unite



class OperationForm(forms.ModelForm):
    #coords_longlat = forms.CharField(max_length=14)
    #coords_lambert = forms.CharField(max_length=30)
    z = forms.FloatField()

    def add3D_to_geom(self):
        return self
    
    class Meta:
        model = Operation
        exclude = ['']

class SondageForm(forms.ModelForm):
    #coords_longlat = forms.CharField(max_length=14)
    #coords_lambert = forms.CharField(max_length=30)
    z = forms.FloatField()

    def add3D_to_geom(self):
        return self
    
    class Meta:
        model = Operation
        exclude = ['']






class MentionInline(admin.TabularInline):
    model = Mention
    extra = 1

class DocumentResource(resources.ModelResource):

    class Meta:
        model = Document
    

class DocumentAdmin(ImportExportModelAdmin):
    resource_class = DocumentResource
    list_display = ('nom_document','auteur','annee','traitement')
    fieldsets = [
        (None, {'fields': (
          ('nom_document','slug'),('auteur','annee'),          
          'commentaire',
          'traitement', 
        )         
        }),
    ]
    inlines = [
        MentionInline,
    ]
    list_filter = ('nom_document','auteur','annee','traitement')
    pass

class MentionResource(resources.ModelResource):

    class Meta:
        model = Mention

class MentionAdmin(ImportExportModelAdmin):
    list_display = ('mention','document','page')
    
    fieldsets = [
        (None, 
        {'fields': (
            ('mention','commentaire'),
            ('page','document'),
            'sequence',     
        ),}
        ,)]
    filter_horizontal = ("sequence",)
    resource_class = MentionResource
    pass

class OperationResource(resources.ModelResource):

    class Meta:
        model = Operation

class OperationAdmin(ImportExportModelAdmin, LeafletGeoAdmin):    
    list_display = ('nom_operation','type_operation','geom_as_text',)
    resource_class = OperationResource
    form = OperationForm
    fieldsets = [
        (None, 
        {'fields': (
            ('nom_operation','slug'),
            ('type_operation','z'),
            #('coords_longlat','coords_lambert','dim3'),            
            ('geom'),   
        ),}
        ,)]
    def geom_as_text(self, obj):
        return obj.geom_as_text()
    pass

class SondageResource(resources.ModelResource):

    class Meta:
        model = Sondage


class SondageAdmin(ImportExportModelAdmin, LeafletGeoAdmin):
    list_display = ('nom_sondage','operation')
    resource_class = SondageResource
    form = SondageForm
    fieldsets = [
        (None, 
        {'fields': (
            ('nom_sondage','operation'),
            #('coords_longlat','coords_lambert','dim3'),
            ('z'),
            ('geom'),   
        ),}
        ,)]
    pass

class ObservationResource(resources.ModelResource):

    class Meta:
        model = Observation

class ObservationAdmin(ImportExportModelAdmin):
    list_display = ('nom_observation','type_observation','sondage','sequence','acces_possible')
    resource_class = ObservationResource
    pass

class UniteResource(resources.ModelResource):

    class Meta:
        model = Unite

class UniteAdmin(ImportExportModelAdmin):
    list_display = ('nom_unite','profondeur','epaisseur','texture_1','texture_2','couleur','nuance_couleur','valeur_couleur','tache','carbonate','type_carbon','structure_1','taille_structure','structure_2','sous_structure','compacite','inclusion','mobilier','interpretation_sedimentaire','interpretation_pedologique','interface','echantillon','autre')
    resource_class = UniteResource
    list_filter = ('nom_unite','profondeur','epaisseur','texture_1','texture_2','couleur','nuance_couleur','valeur_couleur','couleur_MSCC','tache','carbonate','type_carbon','structure_1','taille_structure','structure_2','sous_structure','description_structure','compacite','inclusion','mobilier','perturbation','interpretation_sedimentaire','interpretation_pedologique','interface','echantillon','autre')
    pass


class SequenceResource(resources.ModelResource):

    class Meta:
        model = Sequence

class SequenceAdmin(ImportExportModelAdmin):    
    list_display = ('nom_sequence',)
    filter_horizontal = ("unite",)
    resource_class = SequenceResource
    list_filter = ('nom_sequence', 'unite')
    pass



admin.site.register(Document, DocumentAdmin)
admin.site.register(Mention, MentionAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Sondage, SondageAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Unite, UniteAdmin)
