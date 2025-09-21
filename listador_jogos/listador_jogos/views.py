from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm

def segurancahome(request):
    return render(request,"Login/base.html")

def register(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('segurancahome')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request,'Login/register.html', context)