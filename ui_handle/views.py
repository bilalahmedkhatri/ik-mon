from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def handle(request):
    return HttpResponse('test')


def home_page(request):
    return render(request, 'index.html')
