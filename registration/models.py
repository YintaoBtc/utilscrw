from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from wallet.commands.instruct_wallet import instruct_wallet


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    addr_base = models.CharField(max_length=100, null=True, blank=True)
    balance = models.FloatField(default=0)

    public = models.BooleanField(default=False)

    class Meta:
        ordering = ['user__username']




@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)
        address = instruct_wallet("getnewaddress", [str(instance)])["result"]
        profile_address = Profile.objects.get(user=instance)
        profile_address.addr_base = address
        profile_address.save()
        print("Se acaba de crear un perfil")


