from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faucet(models.Model):
    username = models.CharField(max_length=100)
    ip_user = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    completed = models.BooleanField(default=False, verbose_name="Completo")

    class Meta:
        verbose_name = "faucet"
        verbose_name_plural = "faucets"
        ordering = ['username']

    def __str__(self):
        return self.username
