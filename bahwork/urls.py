"""bahwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from .settings import MEDIA_ROOT
from users import views as user_views
from home import views as home_views
from jobs import views as jobs_views
from shop import views as shop_views
from cart import views as cart_views
from checkout import views as checkout_views

"""These are the urls moved throughout the project. Some are brought in from the apps, i.e. the blog, shop, cart, checkout and jobs urls. The individual extensions within these files are handled within 'urls.py' files within the individual apps."""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('update_profile/', user_views.update_profile, name='update_profile'),
    path('public_profile/<str:profile_id>/', user_views.public_profile, name='public_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('blog/', include('blog.urls')),
    path('jobs/', include('jobs.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('home.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT }),
]

# add static media settings to urlpatterns while in debug mode
#if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Static media url added according to Django documentation
