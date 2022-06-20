from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, get_object_or_404
from .forms import * 

# Create your views here.

def Index(request):
    blogPost = Blog.objects.all()
    return render(request, 'index.html', {'blog':blogPost})


def CreateBlog(request):    
    if request.method == 'POST':
        form = CreateBlogs(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('createblog')
    else:
        form = CreateBlogs()
    return render(request, 'create_blog.html', {'form':form})

def EditBlog(request, pk):
    blogs = Blog.objects.get(id=pk)
    # if request.method =='POST':
    blog_form =  CreateBlogs(request.POST or None, instance = blogs)  
    if blog_form.is_valid():
        blog_form.save()  
        return redirect('index')
    
    return render(request, 'edit_blog.html',{'blogs': blogs})

def DeleteBlog(request, pk):
    blogs = Blog.objects.get(id=pk)
    blogs.delete()

    return render(request, 'index.html',)
