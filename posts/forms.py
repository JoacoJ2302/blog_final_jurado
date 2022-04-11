from django import forms
from .models import Post, Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido',)

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('titulo', 'subtitulo', 'autor', 'contenido', 'imagen')
        
            widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Subtitulo'}),
            'autor' : forms.TextInput(attrs={'class':'form-control','value':'','id':'autor', 'type':'hidden'}),
        }
        

