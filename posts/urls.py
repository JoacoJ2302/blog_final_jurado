from django.urls import path
from posts import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('lista_posts/', views.ListaPosts.as_view(), name='lista_posts'),
    path('ver_post/<pk>/', views.VerPost.as_view(), name='ver_post'),
    path('create_post/', views.CrearPost.as_view(), name='create_post'),
    path('update_post/<pk>/', views.UpdatePost.as_view(), name='update_post'),
    path('delete_post/<pk>/', views.BorrarPost.as_view(), name='delete_post'),
    path('ver_post/<pk>/comentar/',views.AgregarComentario.as_view(), name='comentar'),
    path('like/<pk>', views.me_gusta, name='like_post'),
]