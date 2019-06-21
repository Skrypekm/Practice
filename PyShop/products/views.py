from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('This page is for new products')

