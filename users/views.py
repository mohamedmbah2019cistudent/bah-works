from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post
from jobs.models import Job
from .models import Profile
from django.contrib.auth.decorators import login_required

"""The following functions handle the views for the users app"""
#The register page allows a user to create a new account
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			#Flash the following message on the login page once the user has been created and can login
			messages.success(request, f'Your account has been created, you are now able to log in')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})



#The user whos account it is can click onto this from their profile page and update their information at any time
@login_required
def update_profile(request):
	#Creating instances of our forms
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		#Check to see if the two parts of the form are valid. If so, then save.
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account details have been updated')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)

	#Create context dictionary
	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	#Ensure that context dictionary is included in these parameters
	return render(request, 'users/update_profile.html', context)


#The profile page is for view only by the owner of the account. From here they can upload blogs, jobs etc
@login_required
def profile(request):
	context = {
		'users': Profile,
		'posts': Post.objects.all(),
		'jobs': Job.objects.all()
	}	

	return render(request, 'users/profile.html', context)


#Public profile view is used for other users to be able to see information about another user.
@login_required
def public_profile(request, profile_id):
	context = {
		'profile': Profile.objects.get(id=profile_id),
		'posts': Post.objects.all(),
		'jobs': Job.objects.all()
	}

	return render(request, 'users/public_profile.html', context)
