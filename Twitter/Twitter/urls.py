from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('twitterapp.views',
    # Examples:
     url(r'^$','index',name='index'),
     url(r'^process/$','process',name='process'),
     url(r'^signin/$','sign_in',name="sign_in"),
     url(r'^q/$','q',name="q"),
     url(r'^signout/$','signout',name="sign_out"),
    # url(r'^Twitter/', include('Twitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', include('analytics.urls', namespace='analytics')),
)
