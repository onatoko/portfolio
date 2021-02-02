from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project


def home(request):
    context = {"projects": Project.objects.all()}
    return render(request, "projects/home.html", context)


class ProjectListView(ListView):
    model = Project
    template_name = "projects/home.html"
    context_object_name = projects

    # def get_queryset(self):
    #     projects = Project.objects.all()
    #     return projects

    # def get_context_data(self, **kwargs):
    #     context = super(ImagePostList)
