from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo = models.CharField('titulo', max_length=500, null=False, blank=False)
    subtitulo = models.CharField('subtitulo', max_length=500, null=False, blank=False)
    contenido = RichTextField('contenido', null=False, blank=False)
    imagen = models.ImageField(upload_to='imagenes_post', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes_posts')

    def __str__(self):
        return f'{self.titulo} - Autor: {self.autor}'

    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(args, kwargs)

    def total_likes(self):
        return self.likes.count()

    @property
    def get_comentarios_count(self):
        return self.comentarios.all().count()

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="comentarios", on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField('contenido', null=False, blank=False)

    def __str__(self):
        return f'{self.autor}'