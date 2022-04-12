from django.contrib.auth.models import User
from django.db import models

class User(User):
	# password = models.CharField(max_length = 256)
	
	def Meta():
		proxy = True
	
	def __str__(self):
		return f'I am user: {self.username}'
