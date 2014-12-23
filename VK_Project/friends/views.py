from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from pip import req
from VK.models import UserInfo


class UserFriendsListView(ListView):
    model = UserInfo
    template_name = "friends/friends.html"
    context_object_name = "friends"

    def get_queryset(self):
        qs = UserInfo.objects.get(user=self.request.user).friends.all()
        return qs

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UserFriendsListView, self).dispatch(request, *args, **kwargs)


def add(request, friend_id):
    if request.session.get("friendCount") > 3:
        return HttpResponseRedirect(reverse('profile', kwargs={'user_id': friend_id}))
    else:
        request.session["friendCount"] = request.session.get("friendCount", 1) + 1
        current = UserInfo.objects.get(user=request.user)
        friend = UserInfo.objects.get(user=User.objects.get(id=friend_id))
        current.friends.add(friend)
        return HttpResponseRedirect(reverse('friends:friends'))


def delete(request):
    current = UserInfo.objects.get(user=request.user)
    friend = UserInfo.objects.get(user=User.objects.get(id=request.POST["friendId"]))
    current.friends.remove(friend)
    return HttpResponseRedirect(reverse('friends:friends'))