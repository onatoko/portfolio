from django.db import models
from django.utils import timezone
from PIL import Image


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(" ", "_")
    return f"{name}/images/{filename}"


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
        # test

    def __str__(self):
        return self.category


class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    link = models.URLField(blank=True)
    # image = models.ImageField(
    #     default="default.jpg", upload_to="project_images"
    # )
    # images = models.FileField(blank=True)

    def __str__(self):
        return self.title

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #     max_height = 300
    #     max_width = 300
    #     if img.height > max_height or img.width > max_width:
    #         output_size = (max_height, max_width)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, default=None, on_delete=models.CASCADE
    )
    images = models.FileField(upload_to="project_images")

    def __str__(self):
        return self.project.title
