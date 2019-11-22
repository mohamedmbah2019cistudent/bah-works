from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User

# Imports for app testing
from .apps import UsersConfig

#Imports for models and views testing
from .models import Profile

# Create your tests here.
# Testing the app for the blog section
class TestUsersConfig(TestCase):

    def test_users_app(self):
        self.assertEqual("users", UsersConfig.name)
        self.assertEqual("users", apps.get_app_config("users").name)