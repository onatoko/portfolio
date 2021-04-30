from django.contrib import admin
from .models import Category, Project, Image, ImageAlbum

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(ImageAlbum)
