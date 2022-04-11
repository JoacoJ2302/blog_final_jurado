#Funcionalidades de los post
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from posts.models import Post, Comentario
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from posts.forms import ComentarioForm, PostForm
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseRedirect

def inicio(request):
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset)
        ).distinct()
        return render(request, 'posts/inicio.html', {'posts': posts})
    else:
        todosLosPosts = Post.objects.all().order_by('-fecha_publicacion')
        mostrar = Paginator(todosLosPosts, 3)
        pagina_num = request.GET.get('pagina', 1)
        try:
            posts = mostrar.page(pagina_num)
            numeros = "n" * posts.paginator.num_pages
        except EmptyPage:
            posts = mostrar.page(1)
            numeros = "n" * posts.paginator.num_pages
        return render(request, 'posts/inicio.html', {'posts': posts, 'numeros': numeros})


class ListaPosts(ListView):

    model = Post
    template_name= "posts/lista_post.html"
    ordering = ['-fecha_publicacion']

class VerPost(DetailView):
    
    model = Post
    template_name= "posts/ver_post.html"

    def get_context_data(self,*args, **kwargs):
        contexto= super(VerPost, self).get_context_data(*args, **kwargs)
        numero = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = numero.total_likes()
        contexto['total_likes']= total_likes
        return contexto

class CrearPost(CreateView):

    model = Post
    form_class= PostForm    
    success_url = "/posts/ListaPosts"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Publicar'
        })
        return contexto
class UpdatePost(UpdateView):

    model = Post
    form_class= PostForm 
    success_url = "/posts/ListaPosts"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Editar' 
        })
        return contexto
class BorrarPost(DeleteView):

    model = Post 
    success_url = "/posts/ListaPosts"

class AgregarComentario(CreateView):
    
    model = Comentario
    form_class = ComentarioForm
    template_name = "posts/comentario_form.html"

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    success_url = "/posts"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Comentar'
        })
        return contexto


def me_gusta(request,pk):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('verPost', args=pk))



