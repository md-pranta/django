from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    # return HttpResponse('this is app section')
    return render(req, 'app1.html')
    