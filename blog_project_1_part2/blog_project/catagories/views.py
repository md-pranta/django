from django.shortcuts import render, redirect
from .forms import CatagoryFrom
# Create your views here.
def add_catagory(req):
    catagory_form = CatagoryFrom()
    if req.method == 'POST':
        catagory_form = CatagoryFrom(req.POST)
        if catagory_form.is_valid():
            # print(catagory_form.cleaned_data)
            catagory_form.save()
            return redirect('add_catagory')
    return render(req, 'add_catagory.html',{'form': catagory_form})