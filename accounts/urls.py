from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='signup'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]