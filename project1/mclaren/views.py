from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def driver1(request):
    return HttpResponse("I am not fit for racing with this Mclaren. It's literally a rocket")

def driver2(request):
    return HttpResponse("Rookie?? Nah bro. I'm a pookie🎀 with matured racing mind")