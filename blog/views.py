from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



posts = Post.objects.all()


def home_view(request):
    my_context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', my_context)
    # return HttpResponse("<h1>Blog Home</h1>")


def about_view(request):
    return render(request, 'blog/about.html', {"title": "About"})
