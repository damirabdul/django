from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger

from Blog.models import Post

def index(request):
    return render(request,"Blog/index.html")

def posts(request):
    posts_list = Post.objects.all().order_by("-p_date")
    paginator = Paginator(posts_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(
        request,
        "Blog/posts.html",
        {
            "posts": posts
        }
    )

def new(request):
    if request.POST:
        post = request.POST["post"]
        title = request.POST["title"]
        p = Post(title=title,
                 text=post,
                 p_date=datetime.now()
        )
        p.save()
    return render(
        request,
        "Blog/postCreate.html"
    )