from django.shortcuts import render
from posts.views import buscar_url_avatar

def about_me(request):
    return render(request,'index/about_me.html', {'avatar':buscar_url_avatar(request.user)})