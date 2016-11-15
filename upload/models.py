from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
    pic = models.ImageField(upload_to='photos')
