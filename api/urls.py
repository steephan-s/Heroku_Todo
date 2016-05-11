from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

app_name = 'api'
urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.details.as_view(), name='details'),
    url(r'^sort/', views.todolistview.as_view(), name='todolistview'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

