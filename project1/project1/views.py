from django.http import HttpResponse
def home(req):
    return HttpResponse('this is home page')

def contact(req):
    return HttpResponse("this is contact page")