from django.test import TestCase
from django.apps import apps

#Imports for app testing
from .apps import JobsConfig

#Imports for views testing
from .models import Job, JobFileUpload, JobComment

# Create your tests here.
# Testing the app for the blog section
class TestJobConfig(TestCase):

    def test_jobs_app(self):
        self.assertEqual("jobs", JobsConfig.name)
        self.assertEqual("jobs", apps.get_app_config("jobs").name)

#Testing a model for the blog
class TestJobsModels(TestCase):

    def test_create_job(self):
        job = Job(job_name='New Job', job_overview='Basic job content intro', job_description='Content to go into the textfield', job_location_town='Town', job_location_county='County')
        job.save()
        self.assertEqual(job.job_name, 'New Job')
        self.assertEqual(job.job_overview, 'Basic job content intro')
        self.assertEqual(job.job_description, 'Content to go into the textfield')
        self.assertEqual(job.job_location_town, 'Town')
        self.assertEqual(job.job_location_county, 'County')

    def test_job_file(self):
        job_file = JobFileUpload(file_name='Test file', file_price=2.00, uploaded_file='test.pdf')
        self.assertEqual(job_file.file_name, 'Test file')
        self.assertEqual(job_file.file_price, 2.00)
        self.assertEqual(job_file.uploaded_file, 'test.pdf')

    def test_job_comment(self):
        job_comment = JobComment(comment='Test comment')
        self.assertEqual(job_comment.comment, 'Test comment')

#Testing the views
class TestJobViews(TestCase):

    def test_job_home_page(self):
        jobs_home = self.client.get("/jobs/")
        self.assertEqual(jobs_home.status_code, 200)
        self.assertTemplateUsed(jobs_home, "jobs/home.html")