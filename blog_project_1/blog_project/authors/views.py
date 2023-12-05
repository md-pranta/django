from django.shortcuts import render, redirect
from .forms import AuthorFrom
# Create your views here.
def add_author(req):
    author_form = AuthorFrom()
    if req.method == 'POST':
        author_form = AuthorFrom(req.POST)
        if author_form.is_valid():
            # print(author_form.cleaned_data)
            author_form.save()
            return redirect('add_author')
    return render(req, 'add_author.html',{'form': author_form})