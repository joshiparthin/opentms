from django.contrib import admin
from django.urls import path, include
from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LoginView.logout)
]
