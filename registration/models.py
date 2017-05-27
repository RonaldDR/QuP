from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	profilename = models.OneToOneField(User, related_name='profile')
	course = models.CharField(max_length = 120)
	status = models.CharField(max_length = 120)
	studnum = models.IntegerField()
	yrlevel = models.IntegerField()

	def __str__(self):
		return self.studnum + " : "+ self.name
