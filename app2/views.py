from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app2_fun2(request):
    return HttpResponse('<h1>This is app2_fun2 response</h1>')