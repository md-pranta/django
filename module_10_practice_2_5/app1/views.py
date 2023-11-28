from django.shortcuts import render
import datetime
# Create your views here.

def home(req):
    dic = {'li':['py', 'dic', 'fdf', 5], 'number':4, 'name':"I'm pranta",'d':datetime.datetime.now(),'s':'',
    'data':[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]
    }
    return render(req, 'index.html',dic)

