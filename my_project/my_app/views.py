from django.shortcuts import render, redirect
from . models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    posts = Advertisements.objects.all()
    context = {
        "posts": posts
    }

    return render(request, "my_app/index.html", context)

def post_detail_view(request, post_id):
    post_detail = Advertisements.objects.get(id=post_id)
    post_detail.save()
    return render(request, "my_app/post_detail.html", context={"post": post_detail})



def my_custom_view(request):
    return HttpResponse("Bu bir test səhifəsidir!")
