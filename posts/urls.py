from django.urls import path
from posts import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('lista_posts/', views.ListaPosts.as_view(), name='ListaPosts'),
    path('ver_post/<pk>/', views.VerPost.as_view(), name='verPost'),
    path('crear_post/', views.CrearPost.as_view(), name='CrearPost'),
    path('editar_post/<pk>/', views.UpdatePost.as_view(), name='EditarPost'),
    path('borrar_post/<pk>/', views.BorrarPost.as_view(), name='BorrarPost'),
    path('ver_post/<pk>/comentar/',views.AgregarComentario.as_view(), name='comentar'),
    path('like/<pk>', views.me_gusta, name='likePost'),
]