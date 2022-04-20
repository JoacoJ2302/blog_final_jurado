from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login', views.login_request, name ="Login"),
    path('register', views.register, name ="Register"),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name ="Logout"),
    path('editar_perfil',views.editarPerfil,name='EditarPerfil'),
    path('mis_posts_con_me_gusta',views.postsConMeGustaPropios,name="PostsConMeGustaPropios"),
    path('mi_perfil/', views.mi_perfil, name='MiPerfil'),
]