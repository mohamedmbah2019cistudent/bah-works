from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Registration form to take the fields set up in 
class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



#This will allow us to update our email for the user
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']



#This class allows us to update our image for the user
class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['firstname', 'lastname', 'profile_intro', 'image']