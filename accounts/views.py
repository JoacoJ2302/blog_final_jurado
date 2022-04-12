from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from accounts.forms import UserRegisterForm, UserEditForm
from posts.models import Post


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
    return render (request, "accounts/mi_perfil.html")


def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data
            usuario.username = informacion ['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()
            return render(request, "accounts/bienvenido.html", {"mensaje": "Datos de perfil modificados correctamente"})
    else:
        miFormulario = UserEditForm(
            initial={
                    'username': usuario.username,
                    'email': usuario.email, 
                    'first_name': usuario.first_name, 
                    'last_name': usuario.last_name
                    }
            )
    return render(request, "accounts/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


def postsConMeGustaPropios(request):
    current_user = request.user.id
    posts = Post.objects.filter(likes__id=current_user)
    return render(request, 'accounts/posts_con_megusta.html', {"posts": posts})