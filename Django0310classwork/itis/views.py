# Create your views here.
from django.http import HttpResponse

def groups(request):
    return HttpResponse("Group of ITIS")