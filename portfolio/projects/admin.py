from django.contrib import admin
from .models import Category, Project, ProjectImage

# admin.site.register(Category)
# admin.site.register(Project)
# admin.site.register(ProjectImage)


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
        model = Project


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass
