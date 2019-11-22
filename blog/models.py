from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from django.urls import reverse
from PIL import Image

"""Creating a model for the blog posts. Uses appropriate standard field types from within Python."""
class Post(models.Model):
	title = models.CharField(max_length=100)
	intro = models.CharField(max_length=250)
	content = models.TextField()
	#The image is saved to 'blog_images' within the static file. Is the user does not upload an image, their post will display the 'blog-default.jpg' image
	image = models.ImageField(default='blog-default.jpg', upload_to='blog_images')
	date_posted = models.DateTimeField(default=timezone.now)
	#Foreign key links the user to their blog posts
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	#Resize the image as it's saved so it doesn't take too much space. If no image given then the 'user-default.jpg' image will be used for that user.
	def save(self, **kwargs):

		super(Post, self).save()
		if self.image:
			size = 1200, 700
			post_image = Image.open(self.image)
			post_image.thumbnail(size, Image.ANTIALIAS)
			fh = storage.open(self.image.name, "w")
			post_image.save(fh)
			fh.close()

	class Meta:
		ordering = ['-date_posted']


#Model to allow a user to comment on a blog post.
class PostComment(models.Model):
	comment = models.TextField()	
	comment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
	post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='blog_comments')
	author = models.ForeignKey(User, null=False, default=1, on_delete=models.CASCADE, related_name='blog_comments')

	def __str__(self):
		return self.comment

	class Meta:
		ordering = ['-comment_date']
