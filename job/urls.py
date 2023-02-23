from django.contrib import admin
from django.urls import include, path
from . import views, api

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),

    # api 
    path('api/list', api.job_list_api, name='job_list_api'),
    path('api/list/<int:pk>', api.job_list_api_pk, name='job_list_api_pk'),
]