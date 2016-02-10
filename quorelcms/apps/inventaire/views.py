from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django_tables2   import RequestConfig
from django.utils import timezone
from .models import Document, Mention, Operation, Sequence, Unite, Mention

# Create your views here.
def index(request):
   
    return render(request, 'inventaire/quorelIndex.html')



class DocListView(generic.ListView):
    template_name = 'inventaire/docIndex.html'
    context_object_name = 'latest_document_list'
    queryset = Document.objects.all
    

class DocDetailView(generic.DetailView):
    model = Document
    context_object_name = 'document'
    template_name = 'inventaire/docDetail.html'


class OpMapListView(generic.ListView):
    model = Operation
    template_name = 'inventaire/opMapIndex.html'

class OpMapDetailView(generic.DetailView):
    model = Operation
    template_name = 'inventaire/opMapDetail.html'


class SequenceListView(generic.ListView):
    template_name = 'inventaire/sequenceIndex.html'
    context_object_name = 'sequence_list'
    queryset = Sequence.objects.all

class SequenceDetailView(generic.DetailView):
    model = Sequence
    template_name = 'inventaire/sequenceDetail.html'
    context_object_name = 'sequence_detail'

class UniteDetailView(generic.DetailView):
    model = Unite
    template_name = 'inventaire/uniteDetail.html'
    context_object_name = 'unite_detail'
    
#def unite(request):
#     unite_table = UniteTableFull(Unite.objects.order_by('nom_unite'))
#     RequestConfig(request, paginate=False).configure(unite_table)
     
#     return render(request, 'inventaire/unite_table.html', {'unite_table': unite_table})
class MentionDetailView(generic.DetailView):
    model = Mention
    template_name = 'inventaire/mentionDetail.html'
    context_object_name = 'mention_detail'
    