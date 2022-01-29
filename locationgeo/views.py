from django.shortcuts import render

# Create your views here.
import requests
import json

def index(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_one  = res.text
    location_data = json.loads(location_data_one)
    context = {
        'data': location_data
    }
    return render(request , 'index.html' , context) 