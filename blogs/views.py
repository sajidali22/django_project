from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'NayelH',
        'title': 'Blog 1'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogs/home.html', context)

def about(request):
    return render(request, 'blogs/about.html')