from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import post_save, pre_save
from decouple import config


# Create your models here.
User._meta.get_field('email')._unique = True
