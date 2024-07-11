from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"hello.html",{"name":"Mangesh"})


# def index(request):
#     return HttpResponse("awosomse")