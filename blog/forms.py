from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PostComment


#Form to allow users to type comments on a job to question the creator of a job to get more information
class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']