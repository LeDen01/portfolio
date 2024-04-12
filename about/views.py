from django.shortcuts import render,redirect
from about.models import *
from skills.models import *
from portfolio.models import *
from services.models import *
from testimonials.models import *
from contact.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    person = Person.objects.first()
    skills = Skills.objects.all()
    portfolio = Portfolio.objects.all()
    sercices = Service.objects.all()
    temoignages = Temoignage.objects.all()
    contact = Contact.objects.first()
    return render(request, 'index.html', {'person': person, 'skills': skills, 'portfolio': portfolio, 'services': sercices, 'temoignages': temoignages, 'contact': contact})

def administration(request):
    return render(request, 'administration/administration.html')

def admin_about(request):
    person = Person.objects.first()
    return render(request, 'administration/about/admin_about.html', {'person': person})

def update_about(request):
    person = Person.objects.first()
    if request.method == 'POST':
        description = request.POST['description']
        title = request.POST['title']
        about = request.POST['about']
        more = request.POST['more']
        age = request.POST['age']
        website = request.POST['website']
        degree = request.POST['degree']
        phone = request.POST['phone']
        email = request.POST['email']
        city = request.POST['city']
        freelance = request.POST['freelance']
        person.description = description
        person.title = title
        person.about = about
        person.more = more
        person.age = age
        person.website = website
        person.degree = degree
        person.phone = phone
        person.email = email
        person.city = city
        person.freelance = freelance
        try:
            if request.FILES['image']:
                person.image = request.FILES['image']
            if request.POST['birthday'] == '':
                person.birthday = request.POST['birthday']
        except:
            pass
        messages.success(request, 'Informations have been updated') 
        person.save()
        
        return redirect('/administration/about')
    return render(request, 'administration/about/update.html', {'person': person})