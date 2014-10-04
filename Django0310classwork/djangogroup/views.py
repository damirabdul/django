from django.http import HttpResponse

def home(request):
    return HttpResponse("Our group page")

def sqr(request,number):
    
    return HttpResponse(str(5))