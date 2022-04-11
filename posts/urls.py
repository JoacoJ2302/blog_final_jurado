from django.urls import path
from posts import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('ListaPosts/', views.ListaPosts.as_view(), name='ListaPosts'),
    path('verPost/<pk>/', views.VerPost.as_view(), name='verPost'),
    path('CrearPost/', views.CrearPost.as_view(), name='CrearPost'),
    path('EditarPost/<pk>/', views.UpdatePost.as_view(), name='EditarPost'),
    path('BorrarPost/<pk>/', views.BorrarPost.as_view(), name='BorrarPost'),
    path('verPost/<pk>/comentar/',views.AgregarComentario.as_view(), name='comentar'),
    path('like/<pk>', views.me_gusta, name='likePost'),
]