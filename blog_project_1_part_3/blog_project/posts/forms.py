from django import forms

from .models import Post, Comment


class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author', ]
class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        # exclude = ['author', ]
        fields = ['name', 'email', 'body']