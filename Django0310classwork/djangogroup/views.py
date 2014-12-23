from django.http import HttpResponse
from django.db.models import F
from django.db.models import Q
from models import *

def q(request):
    # h = Teacher.objects.get(id=1)
    # h = School.objects.get(id=1)
    # return HttpResponse("<br>".join([t.name for t in h.teacher_set.all()]))
    # h = Lesson.objects.filter(year__gt=1980).filter(year__lt=1995)
    # h = Teacher.objects.get(name__contains='X')
    # h = Lesson.objects.filter(teacher__school__name__startswith='Hog')
    # h = Lesson.objects.exclude(teacher__school__name__startswith='Hog')

    # h = Team.objects.filter(scored__gt=F('missed'))

    query = ~Q(year__lt=1980) | Q(year__gte=1995)

    # h = Lesson.objects.filter(query)

    h = Lesson.objects.raw("select * from djangogroup_student")


    return HttpResponse("<br>".join([str(t) for t in h]))