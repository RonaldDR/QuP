from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserInfoForm(forms.ModelForm):

        # course = forms.CharField(label='Course', required=True)
        # status = forms.CharField(label='Status', required=True)
        # studnum = forms.DecimalField(label='Student Number', required=True)
        # yrlevel = forms.DecimalField(label='Year Level', required=True)

    # def save(self, commit=True):
    #     instance = super(UserInfoForm, self).save(commit=commit)
    #     instance.profile.first_name = self.cleaned_data['first_name']
    #     instance.profile.last_name = self.cleaned_data['last_name']
    #     instance.profile.course = self.cleaned_data['course']
    #     instance.profile.status = self.cleaned_data['status']
    #     instance.profile.studnum = self.cleaned_data['studnum']
    #     instance.profile.yrlevel = self.cleaned_data['yrlevel']

    #     if commit:
    #         instance.profile.save()
    #     return instance
    class Meta:
        model = UserProfile
        fields = ['profilename', 'course','status','studnum','yrlevel']

class RegistrationForm(UserCreationForm):
   
    class Meta:
        model = User 
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        def save(self,commit = True):
            user = super(RegistrationForm,self).save(commit = False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user