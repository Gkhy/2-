from urllib import request
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    for review in reviews:
        print(review.title, review.content)
    context = {"reviews": reviews}

    return render(request, "pairapp/index.html", context)

def new(request):
    return render(request, "pairapp/new.html")

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(title=title, content=content)

    return redirect('pairapp:index')
