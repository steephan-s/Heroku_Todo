from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.detail, name='detail')  
]

urlpatterns = format_suffix_patterns(urlpatterns)
