from django.conf.urls import patterns, include, url
from views import doc, howto

urlpatterns = patterns('',
    (r'^doc', doc),
    (r'^howto', howto),
)
