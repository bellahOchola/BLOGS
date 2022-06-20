from django import forms
from .models import *

class CreateBlogs(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'description','blog_pic')