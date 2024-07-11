from django.urls import path, include
from . import views

#URLCONF
urlpatterns=[
    path("",views.index,name= "index")
]