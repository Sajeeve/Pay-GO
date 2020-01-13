from django.shortcuts import render , redirect
from . models import Destinations , Includes , Booking , User ,Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request,'index.html')
    
def about(request):
    return render (request,'about.html')

def contact(request):
    if request.method == 'POST':
       name = request.POST['name'] 
       email = request.POST['email']
       subject = request.POST['subject']
       message = request.POST['message']
       
       cnt = Contact(name=name , email=email, subject =subject ,message=message)
       cnt.save()
       messages.info(request,'Sent Successfully ....')
       return render(request,'contact.html')

    else :
        return render(request,'contact.html')

def news(request):
    return render (request,'news.html')

def destinations(request):
    dests = Destinations.objects.all()
    return render (request,'destinations.html', {'dests':dests})

def destinationsingapore(request):
    dests = Destinations.objects.get(name = "Singapore")
    offered_dests = Destinations.objects.exclude(name = "Singapore")
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


def book (request ,dests_id):

        if request.method == 'POST':
            user_name = request.POST['user_name']
            name = User.objects.get(username = user_name)

            destination = request.POST['package']
            dname = Destinations.objects.get(name = destination)
    
            phone = request.POST['phone']
            address = request.POST['address']
            zipcode = request.POST['zipcode']
            visitday = request.POST['visitday']
            no_of_people = request.POST['no_of_people']
            anything_else = request.POST['anything_else']

            payment = request.POST['drop']

            booking = Booking( user_name = name , package = dname, phone=phone , address=address,zipcode=zipcode, visitday =visitday ,  no_of_people= no_of_people, anything_else=anything_else ,payment =payment  )
            booking.save()
            return render(request,'booking_invoice.html')
        else:
            desti = Destinations.objects.get(id = dests_id)
            return render(request,'book.html', {'desti':desti})

def booking_invoice(request,dests_id):
    book = Booking.objects.get(user_name =3)
    return render (request,'booking_invoice.html',{'book':book})


def user_account(request):
    return render(request,'user_account.html')