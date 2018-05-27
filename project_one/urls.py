from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/$', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/admin'}, name='logout'),
    url(r'^admin/imports/', include('app_imports.urls')),
]