from django.urls import path
from django.views.generic import TemplateView
from .views import student_home

student_urlpatterns = [
    path('student/home/', student_home),
    # TemplateView.as_view(template_name="student.html")
]