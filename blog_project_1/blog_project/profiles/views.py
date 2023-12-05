from django.shortcuts import render, redirect
from .forms import ProfileForm
# Create your views here.
def add_profile(req):
    profile_form = ProfileForm()
    if req.method == 'POST':
        profile_form = ProfileForm(req.POST)
        if profile_form.is_valid():
            # print(profile_form.cleaned_data)
            profile_form.save()
            return redirect('add_profile')
    return render(req, 'add_profile.html',{'form': profile_form})