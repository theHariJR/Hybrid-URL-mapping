from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def leclerc(request):
    return HttpResponse("He won at Spa, he wins in Monza!")

def sainz(request):
    return HttpResponse("The DRS is on purpose guys - Lord Sainz")