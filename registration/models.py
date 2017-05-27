from django.db import models
from django.contrib.auth.models import User

class UserStatus(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length = 120)

	def __str__(self):
		return '{} & {}'.format(self.user.username, self.status)