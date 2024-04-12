from django.shortcuts import render,redirect
from contact.models import *

# Create your views here.

def admin_contact(request):
    contact = Contact.objects.first()
    return render(request, 'administration/contact/admin_contact.html', {'contact': contact})

def update_contact(request):
    contact = Contact.objects.first()
    if request.method == 'POST':
        location = request.POST['location']
        email = request.POST['email']
        phone = request.POST['phone']
        contact.location = location
        contact.email = email
        contact.phone = phone
        contact.save()
        return redirect('/administration/contact')
    return render(request, 'administration/contact/update.html', {'contact': contact})