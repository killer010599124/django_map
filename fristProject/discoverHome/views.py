from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.http import HttpResponse
from .models import UserInfo
import json

def home(request):
    return render(request, "registration/home.html")
# Create your views here.
def login(request):
    return render(request, "registration/login.html")
def signup(request):
    return render(request,"registration/signUp.html")
def register(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            
            foo_instance = UserInfo.objects.create(username = data['name'], email = data['email'], password = data['pwd'])
            
            return JsonResponse(data)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def signin(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            infodata = data = json.load(request)
            data = UserInfo.objects.raw('SELECT * FROM user WHERE  email = %s and password = %s', (infodata['email'],infodata['pwd'],))
            
            if data:
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'failed'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    # some error occured
    return JsonResponse({"error": ""}, status=400)
    