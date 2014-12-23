from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from photo.forms import PictureForm


def add(request):
    if request.method == "GET":
        context = {}
        form = PictureForm()
        context["picture_form"] = form
        return render(request, "photo/add.html", context)
    else:
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.owner = request.user
            picture.save()
        return HttpResponseRedirect(reverse('photo:all'))
