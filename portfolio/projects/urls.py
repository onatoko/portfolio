from django.urls import path
from . import views
from .views import ProjectListView

urlpatterns = [
    path("", views.home, name="portfolio-home"),
    path("projects/", ProjectListView.as_view(), name="portfolio-projects"),
]
