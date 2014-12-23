from django.conf.urls import url, patterns
from friends.views import UserFriendsListView

urlpatterns = patterns('friends.views',
                       url(r'^$', UserFriendsListView.as_view(), name="friends"),
                       url(r'^add/(?P<friend_id>\d+)/$', 'add', name="add"),
                       url(r'^delete/$','delete',name="delete")
)

