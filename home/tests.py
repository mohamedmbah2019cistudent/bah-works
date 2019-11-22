from django.test import TestCase
from django.apps import apps

#Imports for app testing
from .apps import HomeConfig

# No models created for home app as pages are static 

# Create your tests here.
# Testing the app for the blog section
class TestHomeConfig(TestCase):

    def test_home_app(self):
        self.assertEqual("home", HomeConfig.name)
        self.assertEqual("home", apps.get_app_config("home").name)

# Testing the home app views
class TestHomeViews(TestCase):

    def test_home_app_page_views(self):
        home = self.client.get("/home/")
        self.assertEqual(home.status_code, 200)
        self.assertTemplateUsed(home, "home/index.html")

        about = self.client.get("/about/")
        self.assertEqual(about.status_code, 200)
        self.assertTemplateUsed(about, "home/about.html")

        contact = self.client.get("/contact/")
        self.assertEqual(contact.status_code, 200)
        self.assertTemplateUsed(contact, "home/contact.html")

        privacy = self.client.get("/privacy/")
        self.assertEqual(privacy.status_code, 200)
        self.assertTemplateUsed(privacy, "home/privacy.html")

        terms = self.client.get("/terms/")
        self.assertEqual(terms.status_code, 200)
        self.assertTemplateUsed(terms, "home/terms.html")
