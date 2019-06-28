from django.db import models
from ckeditor.fields import RichTextField

class Block(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    
    height=models.SmallIntegerField(verbose_name="Peso")
    size = models.FloatField(verbose_name="Tamaño")
    difficulty = models.FloatField(verbose_name="Dificultad")
    
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "block"
        verbose_name_plural = "blocks"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
