from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login', views.login_request, name ="Login"),
    path('register', views.register, name ="Register"),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name ="Logout"),
    path('editar_perfil',views.editar_perfil,name='editar_perfil'),
    path('posts_con_me_gusta',views.posts_con_me_gusta_propios,name="posts_con_me_gusta_propios"),
    path('mi_perfil/', views.mi_perfil, name='MiPerfil'),
]