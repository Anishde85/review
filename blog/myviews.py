from django.shortcuts import render
from django.http import HttpResponse
from blog.models import MyModelName
from blog.forms import GeeksForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required
def hello_geek1(request):
    inp = GeeksForm(request.POST or None)
    if request.method == 'POST' and inp.is_valid():
        title1 = inp.cleaned_data['title']
        content1=inp.cleaned_data['description']
        er=MyModelName.objects.all()
        userw=request.user
        record1=MyModelName(title=title1, content=content1,author=userw)
        record1.save()
        post = [i for i in MyModelName.objects.filter(author=userw)]
        return render(request, "index1.html", {'form':inp,'posts': post})
    else:
        userw = request.user
        post = [i for i in MyModelName.objects.filter(author=userw)]
        return render(request, "index1.html", {'form':inp,'posts': post})