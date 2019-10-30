from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date of edition")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, unique=True)
    title_en = models.CharField(verbose_name="Títle", max_length=200, unique=True)
    content = RichTextField(verbose_name="Contenido")
    content_en = RichTextField(verbose_name="Content")
    image = models.FileField()
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_projects")

    addr_shop = models.CharField(max_length=100)
    addr_donate = models.CharField(max_length=100, null=True, blank=True)
    amount_goal = models.FloatField()
    amount_donate = models.FloatField(null=True, blank=True)

    progress = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    completed = models.BooleanField(default=False, verbose_name="Completo")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['title']

    def __str__(self):
        return self.title
