from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangogroup.views.home'),
    # url(r'^Django0310classwork/', include('Django0310classwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     url(r'^q/', 'djangogroup.views.q'),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
