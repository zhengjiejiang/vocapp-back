from django.db import models
from django.contrib.auth.models import User
import uuid



class Daily(models.Model):
    word = models.CharField(max_length = 255)
    sentence = models.CharField(max_length = 255)
    person = models.CharField(max_length = 255)


class Vocabulary(models.Model):
    word = models.CharField(max_length = 255)
    explantation = models.CharField(max_length = 255)
