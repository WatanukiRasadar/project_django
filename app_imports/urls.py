from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ImportsListView.as_view(), name="imports"),
    url(r'^(?P<pk>\d+)/details', views.ImportDetailView.as_view(), name="import-details"),
    url(r'^upload', views.ImportCreateView.as_view(), name="import-file"),
    url(r'^(?P<pk>\d+)/delete', views.ImportDeleteView.as_view(), name="delete-file"),
]