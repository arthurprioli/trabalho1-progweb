from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from jogos.models import Avaliacao
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request,'seguranca/register.html', context)

def logout(req):
    return render(req, 'seguranca/logout.html')

def jogosView(req):
    return render(req, 'jogos/listaJogos.html')

@login_required
def UserPageView(req):
    return render(req, 'seguranca/userPage.html')

class ProfileView(View):
    def get(self,req,pk, *args, **kwargs):
        usuario = get_object_or_404(User,pk=pk)
        avaliacoes = Avaliacao.objects.order_by("-data").filter(autor=usuario)
        context = {
            "perfil": usuario,
            "avaliacoes": avaliacoes
        }
        return render(req, "perfil/avaliacoesPerfil.html",context)


class CustomLoginView(LoginView):
    """Custom LoginView that redirects users to their personal profile page after login.

    Uses the URL named 'perfil' which expects an int:pk argument (the user's pk).
    """
    template_name = "seguranca/login.html"

    def get_success_url(self):
        # Redirect to /perfil/<pk>/ after successful login
        return reverse('perfil', kwargs={'pk': self.request.user.pk})

