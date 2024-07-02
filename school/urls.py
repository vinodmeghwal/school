from django.contrib import admin
from django.urls import path
from .views import StudentView,SchoolView

urlpatterns = [
    path('school/',SchoolView.as_view()),
    path('student/',StudentView.as_view()),
]
