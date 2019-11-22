from django.urls import path
from .views import home, about, terms, privacy, contact, message_received

"""Url patterns for the home app. Imported into the main urls file."""
urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('contact/', contact, name='contact'),
    path('message_received', message_received, name='message_received')
]