from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_wrold(request):
    return render(request, "base.html")