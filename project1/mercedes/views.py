from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def driver1(request):
    return HttpResponse("Okay Lewsi, it's hammer time")

def driver2(request):
    return HttpResponse("Yabadoobadooo the tyre whisperer")
