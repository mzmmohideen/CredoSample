from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import StudentDetails
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth import authenticate

# Create your views here.
@csrf_exempt
def student_home(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print('username', username, 'password', password)
		auth = authenticate(username = username, password = password)
		print(auth)
		if auth is not None:
			data = StudentDetails.objects.all()
			ser = json.loads(serializers.serialize("json", data))
			ser = [i['fields'] for i in ser]
			return render(request, 'student.html', {'data': ser})
		return HttpResponseRedirect('/')
	else:
		return render(request, 'student.html', {'user': {}})
		# return HttpRedirect()
		# exit()


@csrf_exempt
def student_data(request):
	if request.method == 'GET':
		inp = request.GET.get('name')
		out = []
		data = StudentDetails.objects.filter(student_name=inp)
		print('data', data)
		for _row in data:
			out.append(model_to_dict(_row))
		if out:
			return JsonResponse(out[0])
		return HttpResponse('No Data')
	else:
		print('request.POST', request.body)
		return JsonResponse({'response': 'Not Allowed!'})

class StudentView(DetailView):
	model = StudentDetails