from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def home(request, *args, **kwargs):
    if(request.method == "POST"):
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect("home")
    else:
        form = ReviewForm()
    return render(request, "home.html",{'form':form})