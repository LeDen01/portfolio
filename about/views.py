from django.shortcuts import render
from about.models import *
# Create your views here.

def index(request):
    person = Person.objects.first()
    return render(request, 'index.html', {'person': person})

