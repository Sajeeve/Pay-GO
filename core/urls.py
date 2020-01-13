from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('about', views.about , name='about'),
    path('contact', views.contact , name='contact'),
    path('news', views.news , name='news'),
    path('destinations', views.destinations , name='destinations'),

    path('destinationsingapore', views.destinationsingapore , name='destinationsingapore'),
    path('destinationbali', views.destinationbali , name='destinationbali'),
    path('destinationdubai', views.destinationdubai , name='destinationdubai'),
    path('destinationmalaysia', views.destinationmalaysia , name='destinationmalaysia'),
    path('destinationbangkok', views.destinationbangkok , name='destinationbangkok'),
    path('destinationindia', views.destinationindia , name='destinationindia'),

     path('<int:dests_id>/book',views.book , name='book'),
    path('<int:dests_id>/book/booking_invoice', views.booking_invoice, name='booking_invoice'),
    path('user_account',views.user_account, name='user_account')
    
]
