from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from VK_Project import settings

urlpatterns = patterns('VK.views',
                       url(r'^login', 'sign_in', name="sign_in"),
                       url(r'^$', 'index', name="index"),
                       url(r'^logout', 'exit', name="logout"),
                       url(r'^registration', 'registration', name="registration"),
                       url(r'^profile/(?P<user_id>\d+)/$', 'profile', name="profile"),
                       url(r'^edit', 'edit_profile', name="edit"),
                       url(r'^saveProfile/$', 'save_profile', name='save_profile'),
                       url(r'^delete_post/$', 'delete_post', name='delete_post'),
                       url(r'^all/$', 'all', name='all'),
                       url(r'^addComment/$', 'addComment', name="addComment"),
                       url(r'^deleteComment/$', 'deleteComment', name="deleteComment"),
                       url(r'^friends/', include('friends.urls', namespace='friends')),
                       url(r'^message/', include('message.urls', namespace='message')),
                       url(r'^photo/', include('photo.urls', namespace='photo')),
)

urlpatterns += patterns('',
                        url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)', 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}),
)
