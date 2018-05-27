from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'upload', views.upload, name="upload"),
    url(r'read/(\d)', views.read, name="app-read"),
    url(r'delete/(\d)', views.removeFile, name="app-read"),
]