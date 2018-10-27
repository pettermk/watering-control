from django.http import HttpResponse

def index(request):
    return HttpResponse("--Watering control page--")
