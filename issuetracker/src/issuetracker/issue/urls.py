from django.contrib import admin
from django.urls import path, include
from .views import issue_list, issue_create, issuepriority_create, issuepriority_create_post

urlpatterns = [
    path('list/', issue_list),
    path('new/', issue_create),
    path('priority/new/', issuepriority_create),
    path('priority/new/post', issuepriority_create_post)
]
