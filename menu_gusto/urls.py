from django.urls import path
from .views import *


urlpatterns = [
    path('', dish_info),
]
