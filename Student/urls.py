from django.urls import path
from django.views.generic import TemplateView
from .views import student_home, StudentView, student_data

student_urlpatterns = [
    path('student/home/', student_home),
    path('student/data/', student_data),
    path('student/<pk>/', StudentView.as_view())
    # TemplateView.as_view(template_name="student.html")
]