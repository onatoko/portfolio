from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("", views.home, name="portfolio-home"),
    path("projects/", ProjectListView.as_view(), name="portfolio-projects"),
    path(
        "project/<int:id>", ProjectDetailView.as_view(), name="project-detail"
    ),
]
