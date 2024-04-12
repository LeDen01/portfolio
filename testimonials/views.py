from django.shortcuts import render,redirect
from testimonials.models import *

# Create your views here.

def admin_testimonials(request):
    testimonials = Temoignage.objects.all()
    return render(request, 'administration/testimonials/admin_testimonials.html', {'testimonials': testimonials})

def create_testimonial(request):
    if request.method == 'POST':
        image = request.FILES['image']
        auteur = request.POST['auteur']
        poste = request.POST['poste']
        description = request.POST['description']
        temoignage = Temoignage(auteur=auteur, poste=poste, description=description, image=image)
        temoignage.save()
        return redirect('/administration/testimonials')
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
        temoignage.save()
        return redirect('/administration/testimonials')
    return render(request, 'administration/testimonials/update.html', {'temoignage': temoignage})

def delete_testimonial(request, id):
    testi = Temoignage.objects.get(id=id)
    testi.delete()
    return redirect('/administration/testimonials')