from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job, JobFileUpload, JobComment
from .forms import JobFileUploadForm, JobCommentForm
from django.http import HttpResponseForbidden, HttpResponse
from django.conf import settings
from django.urls import reverse
from django.core.files.storage import FileSystemStorage



"""Rendering the views for the jobs pages. As with the blogs section most will be created with classes"""
#Rendering the jobs home page. Takes context as an argument and displays all the blogs.
def home(request):
	context = {
		'jobs': Job.objects.all()
	}
	return render(request, 'jobs/home.html', context)



#List of jobs using standard ListView imported
class JobListView(ListView):
	model = Job
	template_name = 'jobs/home.html'
	context_object_name = 'jobs'
	ordering = ['-date_posted']
	paginate_by = 9



#Render the job details page
class JobDetailView(DetailView):
    model = Job

    #Get the context data to be able to display the uploaded job files from within the detail view for the uploaded files in 'job_detail.html'.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uploaded_files'] = JobFileUpload.objects.filter().order_by('file_price')
        return context



# Logic to allow the page to show all of the files uploaded to a particular job
class JobFileDisplay(LoginRequiredMixin, ListView):
	model = JobFileUpload
	context = {'uploaded_files': JobFileUpload.objects.all()}



#Function view to show the bids and assign a bid to that job
@login_required
def job_upload_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_authenticated):
                uploaded_files = JobFileUpload.objects.all()
                job = get_object_or_404(Job, pk=pk)
                if request.method == "POST":
                    form = JobFileUploadForm(request.POST, request.FILES)
                    if form.is_valid():
                        uploaded_file = form.save(commit=False)
                        uploaded_file.author = request.user
                        uploaded_file.job = job
                        uploaded_file.save()
                        messages.success(request, f'Your file has been uploaded and is available for view by the project owner.')
                        return redirect('job-detail', pk=job.pk)
                else:
                    form = JobFileUploadForm()

        except User.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'jobs/job_upload.html', {'form': form, 'uploaded_files': uploaded_files, 'job': job})



#Allow the comment creator to update the comment
@login_required
def update_comment_view(request, pk):
    comments = JobComment.objects.all()
    jobs = Job.objects.all()
    comment = get_object_or_404(JobComment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author or request.user.is_superuser):
        if request.method == "POST":
            form = JobCommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment = form.save()
                return redirect('job-detail', comment.job.id)
        else:
            form = JobCommentForm(instance=comment)
    else:
        return HttpResponseForbidden()

    return render(request, 'jobs/job_comment.html', {'form': form, 'jobs': jobs, 'comments': comments, 'job': comment.job})



#Rendering the job create form. Fields uses the fields created in the 'models.py' file
class JobCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Job
    fields = ['job_name', 'job_overview', 'job_description', 'job_location_town', 'job_location_county', 'image']
    success_message = 'Your job has been successfully created.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #Function to display the message when the job is created
    def get_success_message(self, cleaned_data):
        return self.success_message



#Job update form is the same as the create form. Existing information will be already included in the form
class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Job
    fields = ['job_name', 'job_overview', 'job_description', 'job_location_town', 'job_location_county', 'image']
    success_message = ' Your job has been updated'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #Function to display the message when the job is updated
    def get_success_message(self, cleaned_data):
        return self.success_message

    #Stop the user from being able to access another users post
    def test_func(self):
        job = self.get_object()
        if self.request.user == job.author:
            return True
        else:
            return False
		


#Handle the logic to enable the user to be able to delete a blog
class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Job
    success_url = '/jobs/'
    success_message = 'Your job has been deleted'
    fields = ['job_name']

    #Function to display the message when the job is updated
    def get_success_message(self, cleaned_data):
        return self.success_message

    #Stop a user from being able to access another users post
    def test_func(self):
        job = self.get_object()
        if self.request.user == job.author:
            return True
        else:
            return False



#Creating a comment for the jobs
@login_required
def job_comment_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_authenticated):
                comments = JobComment.objects.all()
                job = get_object_or_404(Job, pk=pk)
                jobs = Job.objects.all()
                if request.method == "POST":
                    form = JobCommentForm(request.POST)
                    if form.is_valid():
                        comment = form.save(commit=False)
                        comment.author = request.user
                        comment.job = job
                        comment.save()
                        return redirect('job-detail', pk=job.pk)
                else:
                    form = JobCommentForm()

        except User.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'jobs/job_comment.html', {'form': form, 'jobs': jobs, 'comments': comments, 'job': job})



#Allow the comment creator to update the comment
@login_required
def update_comment_view(request, pk):
    comments = JobComment.objects.all()
    jobs = Job.objects.all()
    comment = get_object_or_404(JobComment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author or request.user.is_superuser):
        if request.method == "POST":
            form = JobCommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment = form.save()
                return redirect('job-detail', comment.job.id)
        else:
            form = JobCommentForm(instance=comment)
    else:
        return HttpResponseForbidden()

    return render(request, 'jobs/job_comment.html', {'form': form, 'jobs': jobs, 'comments': comments, 'job': comment.job})



#Handle the logic to enable the user to be able to delete a comment
class JobCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = JobComment
    template_name = 'jobs/job_comment_confirm_delete.html'
    success_url = '/jobs/'
    fields = ['comment']
    
    #Stop a user from being able to access another users comment
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        else:
            return False


