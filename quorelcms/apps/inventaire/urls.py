from django.conf.urls import patterns, url
from djgeojson.views import GeoJSONLayerView
from . import views
from .views import DocListView, DocDetailView, OpMapListView, Operation, Sequence, UniteDetailView, MentionDetailView


app_name = 'inventaire'
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^document/(?P<slug>[^/]+)', views.DocDetailView.as_view(), name='docDetail'),
    url(r'^document/$', views.DocListView.as_view(), name='docIndex'),
    url(r'^operation/data.geojson', GeoJSONLayerView.as_view(model=Operation, properties=('popupContent',)), name='opData'),
    url(r'^operation/$', views.OpMapListView.as_view(), name='opMapIndex'),
    url(r'^operation/(?P<slug>[^/]+)', views.OpMapDetailView.as_view(), name='opMapDetail'),
    url(r'^sequence/$', views.SequenceListView.as_view(), name='sequenceIndex'),
    url(r'^sequence/(?P<pk>[^/]+)', views.SequenceDetailView.as_view(), name='sequenceDetail'),
    url(r'^mention/(?P<pk>[^/]+)', views.MentionDetailView.as_view(), name='mentionDetail'),
    url(r'^unite/(?P<pk>[^/]+)', views.UniteDetailView.as_view(), name='uniteDetail'),
   # url(r'^unite/$', views.unite, name='unite_table'),
)