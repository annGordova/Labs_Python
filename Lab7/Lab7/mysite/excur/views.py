from django.shortcuts import render
from excur.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def look(request):
    return render(request, 'look.html')

def look_client(request):
    clients = Client.objects.all()
    return render(request, 'look_client.html', context = {'clients':clients})

def look_destination(request):
    destinations = Destination.objects.all()
    return render(request, 'look_destination.html', context = {'destinations':destinations})

def look_guide(request):
    guides = Guide.objects.all()
    return render(request, 'look_guide.html', context = {'guides':guides})
