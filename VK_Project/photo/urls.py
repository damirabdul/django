from django.conf.urls import patterns, url
from django.views.generic import ListView
from photo.models import Picture

urlpatterns = patterns('',
                       url(r'^$',
                           ListView.as_view(model=Picture, template_name="photo/photo_list.html"), name="all"
                       ),
                       url(r'^add/$','photo.views.add',name="add")
)
