from django.shortcuts import render
from posts.views import buscar_url_avatar

def about_me(request):
    try:
        return render(request,'index/about_me.html', {'avatar':buscar_url_avatar(request.user)})
    except:
        return render(request,'index/about_me.html')
