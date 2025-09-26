from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('jogos:home-jogos')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request,'seguranca/register.html', context)

def logout(req):
    return render(req, 'seguranca/logout.html')

@login_required
def UserPageView(req):
    return render(req, 'seguranca/userPage.html')