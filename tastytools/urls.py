from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import user_passes_test
from .views import doc


urlpatterns = patterns('',
    (r'^', user_passes_test(lambda u: u.is_superuser)(doc)),
)
