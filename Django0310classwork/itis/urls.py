from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
     url(r'^groups$', 'itis.views.groups'),
)