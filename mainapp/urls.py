from django.urls import path
from mainapp.views import index, depth

urlpatterns = [
    path('index/', index),
    path('depth/', depth, name='depth')
]