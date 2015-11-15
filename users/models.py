from django.db import models
from authtools.models import AbstractEmailUser
# Create your models here.

class User(AbstractEmailUser):
    full_name = models.CharField('full name', max_length=255, blank=True, null=True)