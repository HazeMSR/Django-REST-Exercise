# Changes
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	email = models.CharField(max_length=255, unique=True)
	
	class Mode(models.IntegerChoices):
		BUYER = 1
		ADMIN = 2

	mode = models.IntegerField(choices = Mode.choices, default = 1)