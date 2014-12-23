from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','Blog.views.index', name='index'),
    url(r'^posts/$', 'Blog.views.posts', name='posts'),
    url(r'^new/$', 'Blog.views.new', name='new'),
    # url(r'^BlogProject/', include('BlogProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
