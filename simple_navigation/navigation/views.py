from django.shortcuts import render

# Create your views here.
def about(req):
    d = {'author':'rahim', 'age':10}
    return render(req, 'about.html', d)

def contact(req):
    return render(req, 'contact.html')
