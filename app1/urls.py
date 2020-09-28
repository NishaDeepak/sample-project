from django.urls import path

app_name='app1'

from app1 import views
urlpatterns=[
    path('fun1/',views.app1_fun1,name='app1_func1'),
]