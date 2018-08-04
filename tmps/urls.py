
from django.urls import path
from . import  views

urlpatterns = [
    path("fliter",views.fliter),
    path("extend",views.extend),
]
