from django.urls import path
from mainapp.views import index, action_

urlpatterns = [
    path('index/', index),
    path('action/', action_, name="action")
]