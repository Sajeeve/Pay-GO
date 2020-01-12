from django.shortcuts import render
from . models import Destinations , Includes

# Create your views here.
def index(request):
    return render (request,'index.html')
    
def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def news(request):
    return render (request,'news.html')

def destinations(request):
    dests = Destinations.objects.all()
    return render (request,'destinations.html', {'dests':dests})

def destinationsingapore(request):
    dests = Destinations.objects.all()
    offered_dests = Destinations.objects.exclude(name = 'dests.name')
    return render (request,'destinations\singapore.html', {'dests':dests , 'offered_dests' : offered_dests})

def destinationbali(request):
    offered_dests = Destinations.objects.all()
    return render (request,'destinations\Bbali.html', {'offered_dests':offered_dests})

def destinationbangkok(request):
    offered_dests = Destinations.objects.all()
    return render (request,'destinations\Bbangkok.html', {'offered_dests':offered_dests})

def destinationdubai(request):
    dests = Destinations.objects.all()
    offered_dests = Destinations.objects.exclude(name = 'dests.name')
    return render (request,'destinations\dubai.html', {'dests':dests , 'offered_dests' : offered_dests})

def destinationindia(request):
    dests = Destinations.objects.all()
    offered_dests = Destinations.objects.exclude(name = 'dests.name')
    return render (request,'destinations\india.html', {'dests':dests , 'offered_dests' : offered_dests})

def destinationmalaysia(request):
    dests = Destinations.objects.all()
    offered_dests = Destinations.objects.exclude(name = 'dests.name')
    return render (request,'destinations\malaysia.html', {'dests':dests , 'offered_dests' : offered_dests})

