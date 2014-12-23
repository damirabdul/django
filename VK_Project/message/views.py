from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from message.models import Message


def delete(request):
    message = Message.objects.get(id=request.POST["messageId"])
    message.delete()
    if request.POST["place"] == "im" :
        return HttpResponseRedirect(reverse('message:im'))
    else :
        return HttpResponseRedirect(reverse('message:om'))


def write(request,userId):
    if request.POST:
        to = User.objects.get(id=userId)
        message = Message(to_who=to,from_whom=request.user,message_text=request.POST["text"],message_date=timezone.now())
        message.save()
        return HttpResponseRedirect(reverse('message:om'))
    else:
        to = User.objects.get(id=userId)
        return render(request,"messages/write.html",{"to":to})


class InputMessagesView(ListView):
    model = Message
    template_name = "messages/input.html"
    context_object_name = "message"

    def get_queryset(self):
        qs = Message.objects.filter(to_who=self.request.user)
        return qs

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(InputMessagesView, self).dispatch(request, *args, **kwargs)

class OutputMessagesView(ListView):
    model = Message
    template_name = "messages/output.html"
    context_object_name = "message"

    def get_queryset(self):
        qs = Message.objects.filter(from_whom=self.request.user)
        return qs

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(OutputMessagesView, self).dispatch(request, *args, **kwargs)
