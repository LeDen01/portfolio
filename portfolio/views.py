from django.shortcuts import render,redirect
from portfolio.models import *
from django.contrib import messages

# Create your views here.

def admin_portfolio(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'administration/portfolio/admin_portfolio.html', {'portfolio': portfolio})

def delete_portfolio(request, id):
    portfolio = Portfolio.objects.get(id=id)
    messages.success(request, 'Portfolio deleted')
    portfolio.delete()
    return redirect('/administration/portfolio')

def create_portfolio(request):
    if request.method == 'POST':
        filter = request.POST['filter']
        try:
            if request.FILES['image']:
                image = request.FILES['image']
                portfolio = Portfolio(image=image, filter=filter)
        except:
            messages.error(request, 'Please select an image')
            return redirect('/administration/portfolio/create')
        messages.success(request, 'New portfolio created') 
        portfolio.save()
        return redirect('/administration/portfolio')
    return render(request, 'administration/portfolio/create.html')

def update_portfolio(request, id):
    portfolio = Portfolio.objects.get(id=id)
    if request.method == 'POST':
        filter = request.POST['filter']
        portfolio.filter = filter
        try:
            if request.FILES['image']:
                portfolio.image = request.FILES['image']
        except:
            pass
        messages.success(request, 'Informations have been updated') 
        portfolio.save()
        return redirect('/administration/portfolio')
    return render(request, 'administration/portfolio/update.html', {'portfolio': portfolio})