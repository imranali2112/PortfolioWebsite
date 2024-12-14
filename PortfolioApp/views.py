from django.shortcuts import render, HttpResponse
from .import models
from django.contrib import messages
# Create your views here.
def index(request):
    about = models.About.objects.all()
    project = models.Project.objects.all()
    context = {
        'abouts': about,
        'project': project
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        models.Contact.objects.create(name = name, email = email, subject = subject, message = message)
        messages.success(request=request, message="Your message has been successfully sent.")
    return render(request, 'index.html')

def project_detail(request, project_id):
    project = models.Project.objects.get(id=project_id)
    context = {
        'project': project
    }
    return render(request, 'project.html', context)