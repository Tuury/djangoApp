from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from reservas.models import User
from consorcio.serializers import UserSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = User.objects.all()
	if request.method == 'GET':
		serializer = UserSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def login(request):
	data = User.objects.filter(id='1')
	if request.method == 'GET':
		serializer = UserSerializer(data, many=False)
		return JsonResponse(serializer.data, safe=False)
