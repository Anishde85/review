from django.shortcuts import render
from django.http import HttpResponse
from blog.models import MyModelName
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required
def hello_geek1(request):
    userw = request.user
    post = [i for i in MyModelName.objects.filter(author=userw)]
    return render(request, "index1.html", {'posts': post})