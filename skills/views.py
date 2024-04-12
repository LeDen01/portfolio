from django.shortcuts import render,redirect
from skills.models import *

# Create your views here.

def admin_skills(request):
    skills = Skills.objects.all()
    return render(request, 'administration/skills/admin_skills.html', {'skills': skills})

def create_skills(request):
    if request.method == 'POST':
        langage = request.POST['langage']
        level = request.POST['level']
        skill = Skills(langage=langage, level=level)
        skill.save()
        return redirect('/administration/skills')
    return render(request, 'administration/skills/create.html')

def delete_skills(request, id):
    skill = Skills.objects.get(id=id)
    skill.delete()
    return redirect('/administration/skills')

def update_skill(request, id):
    skill = Skills.objects.get(id=id)
    if request.method == 'POST':
        langage = request.POST['langage']
        level = request.POST['level']
        skill.langage = langage
        skill.level = level
        skill.save()
        return redirect('/administration/skills')
    return render(request, 'administration/skills/update.html', {'skill': skill})