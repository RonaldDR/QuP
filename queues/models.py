from django.db import models
from django.contrib.auth.models import User

class Queue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user.username)