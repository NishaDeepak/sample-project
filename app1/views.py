from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app1_fun1(request):
    return HttpResponse('This is app1_fun1 response')
