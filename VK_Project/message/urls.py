from django.conf.urls import url, patterns
from message.views import InputMessagesView, OutputMessagesView

urlpatterns = patterns('message.views',
                       url(r'^write/(?P<userId>\d+)/$', 'write', name="write"),
                       url(r'^im/$',InputMessagesView.as_view(),name="im"),
                       url(r'^om/$',OutputMessagesView.as_view(),name="om"),
                       url(r'^delete/$', 'delete', name="delete")
)