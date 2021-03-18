from django.contrib import admin
from django.urls import path
from blog.views import hello_geek
from blog.forms import *
from users.views import register,logout_view,login_view
from django.contrib.auth import views
from blog.myviews import hello_geek1
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/',admin.site.urls),
    path('blog/', hello_geek,name="home"),
    path('',register,name='verify'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('blog/my/',hello_geek1,name='myblog')
]
urlpatterns += staticfiles_urlpatterns()
