from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from blog.models import Post
from jobs.models import Job

# Create your views here.

"""The pages for the home app have been rendered using functions"""
#Home page rendered here. The context is imported into the render containing posts and jobs, limiting the amount of the blogs and jobs.
def home(request):
    context = {
		'posts': Post.objects.all()[:6],
		'jobs': Job.objects.all()[:4]
	}
    return render(request, 'home/index.html', context)



#Rendering the about page
def about(request):
    return render(request, 'home/about.html')



#Rendering the terms and conditions page
def terms(request):
    return render(request, 'home/terms.html')



#Rendering the privacy policy
def privacy(request):
    return render(request, 'home/privacy.html')



#Rendering the contacts page. Handles the logic for sending email to site owner.
def contact(request):
    if request.method == 'POST':
        contact_email = request.POST['email']
        message = request.POST['message']

        #Setting the message to send to the site owner
        send_mail('CADWork message from ' + contact_email, 
            message, 
            settings.EMAIL_HOST_USER, 
            [settings.EMAIL_HOST_USER], 
            fail_silently=False
        )
        #Redirect the user who sends the message to the message received
        return redirect('message_received')
    return render(request, 'home/contact.html')


#Rendering the message received page
def message_received(request):
    return render(request, 'home/message_received.html')