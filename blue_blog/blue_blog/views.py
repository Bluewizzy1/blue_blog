from django.shortcuts import render

def detail(request, slug):
    post = get_object_or_404(Post, )