from django.contrib import admin
from .models import Comentario, Post


admin.site.register(Post)
admin.site.register(Comentario)
