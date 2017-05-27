from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	course = forms.CharField(label='Course', required=True)
	status = forms.CharField(label='Status', required=True)
	studnum = forms.DecimalField(label='Student Number', required=True)
	yrlevel = forms.DecimalField(label='Course', required=True)
	
	class Meta:
		model = User 
		fields = (
			'username',
			'first_name',
			'last_name',
			'course',
			'yrlevel',
			'studnum',
			'status'
		)
		def save(self,commit = True):
			user = super(RegistrationForm,self).save(commit = False)
			user.first_name = self.cleaned_data['first_name']
			user.last_name = self.cleaned_data['last_name']
			user.course = self.cleaned_data['course']
			user.status = self.cleaned_data['status']
			user.studnum = self.cleaned_data['studnum']
			user.yrlevel = self.cleaned_data['yrlevel']
			if commit:
				user.save()
			return user