from django.urls import path

from myapp .views import *

urlpatterns = [
    path('', index),
    path('home/', home),
]
