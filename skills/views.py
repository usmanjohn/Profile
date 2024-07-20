from django.shortcuts import render

from .models import Skill, Tool, Owner, Project, Education,Experience,Volunteer,Certificate,Interest, Awards


def home(request):
    owner = Owner.objects.first()  # Assuming you have only one owner
    skills = Skill.objects.filter(owner=owner)
    recent_projects = Project.objects.filter(owner=owner).order_by('-created_at')[:4]
    
    context = {
        'owner': owner,
        'skills': skills,
        'recent_projects': recent_projects,
    }
    #return render(request, 'home.html', context)

def profile_view(request):
    owner = Owner.objects.first()  # Assuming you have only one owner
    context = {
        'owner': owner,
        'skills': Skill.objects.filter(owner=owner),
        'projects': Project.objects.filter(owner=owner),
        'experiences': Experience.objects.filter(owner=owner).order_by('-start_date'),
        'education': Education.objects.filter(owner=owner).order_by('-start_year'),
        'awards': Awards.objects.filter(owner=owner).order_by('-given_date'),
        'certificates': Certificate.objects.filter(owner=owner).order_by('-date_achieved'),
    }
    return render(request, 'home.html', context)