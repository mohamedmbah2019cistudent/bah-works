from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User

#Imports for app testing
from .apps import BlogConfig

#Imports for views testing
from .models import Post, PostComment

# Create your tests here.
# Testing the app for the blog section
class TestBlogConfig(TestCase):

    def test_blog_app(self):
        self.assertEqual("blog", BlogConfig.name)
        self.assertEqual("blog", apps.get_app_config("blog").name)

#Testing a model for the blog
class TestBlogModels(TestCase):

    def test_create_post(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='passwordtest')
        self.client.login(username='testuser', password='passwordtest')
        post = Post(title='Blog post', intro='Basic blog post content intro', content='Content to go into the textfield', author_id=user.id)
        post.save()
        self.assertEqual(post.author.username, 'testuser')
        self.assertEqual(post.title, 'Blog post')
        self.assertEqual(post.intro, 'Basic blog post content intro')
        self.assertEqual(post.content, 'Content to go into the textfield')

    def test_post_comment(self):
        User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='passwordtest')
        self.client.login(username='testuser', password='passwordtest')
        post_comment = PostComment(comment='Test comment', post_id='1')
        post_comment.save() 
        self.assertEqual(post_comment.post_id, '1')
        self.assertEqual(post_comment.comment, 'Test comment')
        self.assertEqual(post_comment.author.username, 'testuser')
        
#Testing the views
class TestBlogViews(TestCase):
    def test_get_home_blog_page(self):
        blog_home = self.client.get("/blog/")
        self.assertEqual(blog_home.status_code, 200)
        self.assertTemplateUsed(blog_home, "blog/home.html")