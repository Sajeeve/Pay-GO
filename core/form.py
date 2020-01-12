from django.forms import ModelForm
from . models import Booking

class BookForm(ModelForm):
        model = Booking
        fields=('name')