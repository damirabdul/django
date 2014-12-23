import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from VK.forms import LoginForm, AvatarForm
from VK.models import UserInfo, Post, Comment


def no_auth_please(v):
    def wrapper(request, *a, **k):
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse('profile', kwargs={'user_id': user.id}))
        else:
            return v(request, *a, **k)

    return wrapper


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('profile', kwargs={'user_id': request.user.id}))
    else:
        return HttpResponseRedirect(reverse('sign_in'))


@no_auth_please
def sign_in(request):
    if request.POST:
        f = LoginForm(request.POST)
        if f.is_valid():
            user = authenticate(
                username=f.cleaned_data["login"],
                password=f.cleaned_data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('profile', kwargs={'user_id': user.id}))
            else:
                return HttpResponseRedirect(reverse('sign_in'))
    else:
        login_form = LoginForm()
        context = {"login_form": login_form}
        return render(request, "VK/login.html", context)


@no_auth_please
def registration(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        check = User.objects.filter(username=username)
        if check:
            return render(request, "VK/registration.html", {"warning": "true"})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user = User.objects.get(username=username)
            info = UserInfo(user=user, sex=sex, birthday=birthday,avatar="avatars/defaultavatar.jpg")
            info.save()
            logged = authenticate(username=username, password=password)
            login(request, logged)
            return HttpResponseRedirect(reverse('profile', kwargs={'user_id': user.id}))
    else:
        return render(request, "VK/registration.html")


@login_required(login_url=reverse_lazy("sign_in"))
def exit(request):
    logout(request)
    return HttpResponseRedirect(reverse("sign_in"))


@login_required(login_url=reverse_lazy("sign_in"))
def profile(request, user_id):
    if request.POST:
        post_text = request.POST["text"]
        to_who = User.objects.get(id=user_id)
        post = Post(post_text=post_text,post_date=timezone.now(),from_whom=request.user,to_who=to_who)
        post.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'user_id': to_who.id}))
    else:
        user = User.objects.get(id=user_id)
        return render(request, "VK/profile.html",
                      {
                          "info": UserInfo.objects.get(user=user),
                          "friends": UserInfo.objects.get(user=request.user).friends.all(),
                          "posts": Post.objects.filter(to_who=user).order_by("-post_date")
                      }
        )


@login_required(login_url=reverse_lazy("sign_in"))
def edit_profile(request):
    p = UserInfo.objects.filter(user=request.user)
    if request.method == "GET":
        context = {}
        if p.exists():
            form = AvatarForm(instance=p[0])
            context["avatar"] = p[0].avatar
        else:
            form = AvatarForm()
        context["avatar_form"] = form
        context["username"] = request.user.username
        return render(request, "VK/edit.html", context)
    else:
        if p.exists():
            form = AvatarForm(request.POST, request.FILES, instance=p[0])
        else:
            form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            userinfo = form.save(commit=False)
            userinfo.user = request.user
            userinfo.save()

        return HttpResponseRedirect(reverse("edit"))


def save_profile(request):
    birthday = request.POST["birthday"]
    city = request.POST["city"]
    interests = request.POST["interests"]
    userinfo = UserInfo.objects.get(user=request.user)
    if userinfo:
        # info = UserInfo(id = userinfo.id,birthday = birthday,city = city, interests = interests)
        # info.save()
        userinfo.city = city
        userinfo.birthday = birthday
        userinfo.interests = interests
        userinfo.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': request.user.id}))

def delete_post(request):
    if request.POST:
        postId = request.POST["postId"]
        Post.objects.get(id=postId).delete()
        return HttpResponse('OK')
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def all(request):
    if request.POST:
        users = UserInfo.objects.all()
        if request.POST["name"]:
            users = users.filter(user__username__icontains=request.POST["name"])
        if request.POST["sex"]:
            users = users.filter(sex=request.POST["sex"])
        if request.POST["from"]:
            users = users.filter(Q(birthday__gte=request.POST["from"]))
        if request.POST["to"]:
            users = users.filter(Q(birthday__lt=request.POST["to"]))
        return render(request,"VK/all.html",{"users":users})
    else:
        return render(request,"VK/all.html",{"users":UserInfo.objects.raw("select * from VK_userinfo")})

def addComment(request):
    post = Post.objects.get(id=request.POST["postId"])
    comment = Comment(post=post,comment_date=timezone.now(),owner=request.user,comment_text=request.POST["comment"])
    comment.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': request.POST["userId"]}))

def deleteComment(request):
    comment=Comment.objects.get(id=request.POST["commentId"]).delete()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': request.POST["userId"]}))

