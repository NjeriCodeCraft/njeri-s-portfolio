from django.shortcuts import render
from .models import *

def portfolio(request):
    profile = Profile.objects.first()
    social_media = SocialMedia.objects.filter(profile=profile)
    projects = Project.objects.all()
    skills = Skill.objects.all()
    tools = Tool.objects.all()
    education = Education.objects.all()
    certificates = Certificate.objects.all()
    work_experience = WorkExperience.objects.all()
    
    context = {
        'profile': profile,
        'social_media': social_media,
        'projects': projects,
        'skills': skills,
        'tools': tools,
        'education': education,
        'certificates': certificates,
        'work_experience': work_experience,
    }
    return render(request, 'main/portfolio.html', context)