from django.db import models
from django.contrib.auth.models import User

class Window1Queue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user.username)

class Window2Queue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user.username)

class Window3Queue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user.username)

class Window4Queue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user.username)

class Window5Queue(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user.username)