from django.shortcuts import render,redirect
from testimonials.models import *
from django.contrib import messages

# Create your views here.

def admin_testimonials(request):
    testimonials = Temoignage.objects.all()
    return render(request, 'administration/testimonials/admin_testimonials.html', {'testimonials': testimonials})

def create_testimonial(request):
    if request.method == 'POST':
        auteur = request.POST['auteur']
        poste = request.POST['poste']
        description = request.POST['description']
        try:
            if request.FILES['image']:
                image = request.FILES['image']
                temoignage = Temoignage(auteur=auteur, poste=poste, description=description, image=image)
        except:
            messages.error(request, 'Please select an image')
            return redirect('/administration/testimonials/create')
        if auteur != "" and poste != "" and description != "":
            messages.success(request, 'New testimonial created') 
            temoignage.save()
            return redirect('/administration/testimonials')
        else :
            messages.error(request, 'Please fill all fields')
            return redirect('/administration/testimonials/create')
        # temoignage.save()
        # messages.success(request, 'New testimonial created') 
        # return redirect('/administration/testimonials')
    return render(request, 'administration/testimonials/create.html')

def update_testimonial(request, id):
    temoignage = Temoignage.objects.get(id=id)
    if request.method == 'POST':
        temoignage.auteur = request.POST['auteur']
        temoignage.poste = request.POST['poste']
        temoignage.description = request.POST['description']
        try:
            if request.FILES['image']:
                temoignage.image = request.FILES['image']
        except:
            pass
        messages.success(request, 'Informations have been updated') 
        temoignage.save()
        return redirect('/administration/testimonials')
    return render(request, 'administration/testimonials/update.html', {'temoignage': temoignage})

def delete_testimonial(request, id):
    testi = Temoignage.objects.get(id=id)
    messages.success(request, 'Testimonial deleted')
    testi.delete()
    return redirect('/administration/testimonials')