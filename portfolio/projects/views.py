from django.shortcuts import render
from .models import Project


def home(request):
    context = {"projects": Project.objects.all()}
    return render(request, "projects/home.html", context)
