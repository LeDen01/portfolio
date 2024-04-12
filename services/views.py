from django.shortcuts import render,redirect
from services.models import *

# Create your views here.

def admin_services(request):
    services = Service.objects.all()
    return render(request, 'administration/services/admin_services.html', {'services': services})

def delete_services(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('/administration/services')

def create_services(request):
    if request.method == 'POST':
        icone = request.POST['icone']
        title = request.POST['title']
        description = request.POST['description']
        service = Service(icone=icone, title=title, description=description)
        service.save()
        return redirect('/administration/services')
    return render(request, 'administration/services/create.html')

def update_services(request, id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        service.icone = request.POST['icone']
        service.title = request.POST['title']
        service.description = request.POST['description']
        service.save()
        return redirect('/administration/services')
    return render(request, 'administration/services/update.html', {'service': service})