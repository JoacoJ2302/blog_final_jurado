from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from accounts.forms import UserRegisterForm, UserEditForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
from posts.views import buscar_url_avatar
from .models import Avatar

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'accounts/bienvenido.html', {"mensaje": f"El usuario {username} se ha creado con éxito"})
        else:
            return render(request, 'accounts/bienvenido.html', {"mensaje": "El usuario no se ha creado"})  
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/registro.html', {"form": form})


def login_request(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                    username=data['username'], password=data['password'])
                if user is not None:
                    login(request, user)
                    return render(request, "accounts/bienvenido.html", {"mensaje": f"Bienvenido {user.get_username()}"})
                else:
                    return render(request, "accounts/login.html", {"mensaje": "Datos incorrectos"})
            else:
                return render(request, "accounts/login.html", {"mensaje": "El usuario no existe"})
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {'form': form})


def mi_perfil (request):
    try:
        return render (request, "accounts/mi_perfil.html", {'avatar':buscar_url_avatar(request.user)}) 
    except:
        return render (request, 'accounts/mi_perfil.html')
    
@login_required
def editar_perfil(request):

    user_extension_logued, _ = Avatar.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES)
        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data
            request.user.username = informacion ['username']
            request.user.email = informacion['email']
            request.user.password1 = informacion['password1']
            request.user.password2 = informacion['password1']
            request.user.first_name = informacion['first_name']
            request.user.last_name = informacion['last_name']
            user_extension_logued.imagen = informacion['avatar']
            
            request.user.save()
            user_extension_logued.save()
            return redirect ('MiPerfil')
        else:
            return render(request, 'accounts/editar_perfil.html', {'miFormulario': miFormulario})
    else:
        miFormulario = UserEditForm(
            initial={
                    'username': request.user.username,
                    'email': request.user.email, 
                    'first_name': request.user.first_name, 
                    'last_name': request.user.last_name
                    }
            )
    return render(request, "accounts/editar_perfil.html", {"miFormulario": miFormulario})


def posts_con_me_gusta_propios(request):
    current_user = request.user.id
    posts = Post.objects.filter(likes__id=current_user)
    return render(request, 'accounts/posts_con_megusta.html', {"posts": posts})