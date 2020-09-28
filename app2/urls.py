from django.urls import path

app_name='app2'

from app2 import views
urlpatterns=[
    path('fun2/',views.app2_fun2,name='app2_func2'),
]