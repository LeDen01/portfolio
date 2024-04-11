from django.shortcuts import render
from about.models import *
from skills.models import *
from portfolio.models import *
from services.models import *

# Create your views here.

def index(request):
    person = Person.objects.first()
    skills = Skills.objects.all()
    portfolio = Portfolio.objects.all()
    sercices = Service.objects.all()
    return render(request, 'index.html', {'person': person, 'skills': skills, 'portfolio': portfolio, 'services': sercices})

