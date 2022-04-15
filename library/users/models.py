# Changes
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	email = models.CharField(max_length=255, unique=True)
	username = models.CharField(max_length=255, unique=True)

	class Type(models.IntegerChoices):
		BUYER = 1
		ADMIN = 2

	type = models.IntegerField(choices = Type.choices, default = 1)