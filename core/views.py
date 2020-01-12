from django.shortcuts import render , redirect
from . models import Destinations , Includes , Booking


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
       
        user = User.objects.create_user(first_name=first_name , last_name=last_name, username =user_name ,email=email,password=password1)
        user.save()
        return redirect('/')
    else:
        return render(request,'contact.html')

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

def booking_invoice(request):
    book = Booking.objects.get(id=4)
    return render (request,'booking_invoice.html',{'book':book})

def book (request):
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            email = request.POST.get('email')
            phone = request.POST['phone']
            address = request.POST['address']
            zipcode = request.POST['zipcode']
            visitday = request.POST['visitday']
            # package = request.POST['package']
            no_of_people = request.POST['no_of_people']
            anything_else = request.POST['anything_else']

            payment = request.POST['drop']

            booking = Booking( user_name=user_name, first_name = first_name, last_name=last_name, email=email, phone=phone , address=address,zipcode=zipcode, visitday =visitday ,  no_of_people= no_of_people, anything_else=anything_else ,payment =payment  )
            booking.save()
            return render(request,'index')
        else:
            return render(request,'book.html')

def user_account(request):
    return render(request,'user_account.html')