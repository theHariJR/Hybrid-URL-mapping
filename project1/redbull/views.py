from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def max(request):
    return HttpResponse("<marquee><h1>Tu tu tu duuuu Max verstappen👿</h1></marquee>")

def perez(request):
    return HttpResponse("<marquee><h1>I really don't know how I'm still racing for Redbull</h1></marquee>")