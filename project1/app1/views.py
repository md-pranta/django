from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def courses(req):
    return HttpResponse('this is courses')
def about(req):
    return HttpResponse('this is About section')