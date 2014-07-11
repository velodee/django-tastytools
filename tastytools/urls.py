from django.conf.urls import patterns, include, url
from .views import doc

urlpatterns = patterns('',
    (r'^', doc),
)
