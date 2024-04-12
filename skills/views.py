from django.shortcuts import render,redirect
from skills.models import *
from django.contrib import messages

# Create your views here.

def admin_skills(request):
    skills = Skills.objects.all()
    return render(request, 'administration/skills/admin_skills.html', {'skills': skills})

def create_skills(request):
    if request.method == 'POST':
        langage = request.POST['langage']
        level = request.POST['level']
        if langage != "" and level != "":
            skill = Skills(langage=langage, level=level)
            messages.success(request, 'New skill created') 
            skill.save()
            return redirect('/administration/skills')
        else :
            messages.error(request, 'Please fill all fields')
            return redirect('/administration/skills/create')
    return render(request, 'administration/skills/create.html')

def delete_skills(request, id):
    skill = Skills.objects.get(id=id)
    messages.success(request, 'Skill deleted')
    skill.delete()
    return redirect('/administration/skills')

def update_skill(request, id):
    skill = Skills.objects.get(id=id)
    if request.method == 'POST':
        langage = request.POST['langage']
        level = request.POST['level']
        skill.langage = langage
        skill.level = level
        messages.success(request, 'Informations have been updated') 
        skill.save()
        return redirect('/administration/skills')
    return render(request, 'administration/skills/update.html', {'skill': skill})