from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='')
    name = models.CharField(max_length=120, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = "UserProfile"


def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)

