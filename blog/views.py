from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    
    return render(request, "blogs/blog.html", {'blogs' : blogs} ) 

def blog_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'blogs/blog_detail.html', {'blog': post})

