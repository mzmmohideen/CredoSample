from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student_home(request):
	return render(request, 'student.html')