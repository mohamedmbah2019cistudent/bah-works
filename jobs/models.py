from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from django.urls import reverse
from PIL import Image


"""Creating the classes for the jobs"""
#The job model will take information when the user fills in the form.
class Job(models.Model):
	job_name = models.CharField(max_length=100, default='Default Project Name')
	job_overview = models.CharField(max_length=250, default='Default Project Overview')
	job_description = models.TextField()
	job_location_town = models.CharField(max_length=30)
	job_location_county = models.CharField(max_length=25)
	#If the user does not save an image, 'job-default.jpg' will be used
	image = models.ImageField(default='job-default.jpg', upload_to='job_images')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, related_name='jobs', null=False, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.job_name
	
	def get_absolute_url(self):
		return reverse('job-detail', kwargs={'pk': self.pk})

	#Resize the image as it's saved so it doesn't take too much space. If no image given then the 'user-default.jpg' image will be used for that user.
	def save(self, **kwargs):

		super(Job, self).save()
		if self.image:
			size = 1200, 700
			job_image = Image.open(self.image)
			job_image.thumbnail(size, Image.ANTIALIAS)
			fh = storage.open(self.image.name, "w")
			job_image.save(fh)
			fh.close()

	class Meta:
		ordering = ['-date_posted']



#Model to handle the upload of files on the Active Job pages
class JobFileUpload(models.Model):
	file_name = models.CharField(max_length=100)
	file_price = models.DecimalField(max_digits=7, decimal_places=2, default=10)
	uploaded_file = models.FileField(upload_to='job_files')
	author = models.ForeignKey(User, max_length=100, related_name='uploaded_files', null=False, default=1, on_delete=models.CASCADE)
	job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='uploaded_files')

	def __str__(self):
		return self.file_name



#Model to allow a user to comment on the job. Allows for users to ask the job creator questions about their job.
class JobComment(models.Model):
	comment = models.TextField()	
	comment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
	job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, null=False, default=1, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return self.comment

	class Meta:
		ordering = ['-comment_date']