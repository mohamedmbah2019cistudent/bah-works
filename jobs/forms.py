from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import JobFileUpload, JobComment


#Form to allow users to upload files to a job
class JobFileUploadForm(forms.ModelForm):
    class Meta:
        model = JobFileUpload
        fields = ['file_name', 'file_price', 'uploaded_file']



#Form to allow users to type comments on a job to question the creator of a job to get more information
class JobCommentForm(forms.ModelForm):
    class Meta:
        model = JobComment
        fields = ['comment']