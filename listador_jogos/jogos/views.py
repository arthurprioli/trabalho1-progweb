from django.shortcuts import render, get_object_or_404
from jogos.models import Jogo
from jogos.forms import JogoModel2Form
from django.views.generic import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy


class JogoListView(View):
    def get(self, req, *args, **kwargs):
        jogos = Jogo.objects.all()
        contexto = {'jogos': jogos}
        return render(
            req,
            'jogos/listaJogos.html',
            contexto
        )


class JogoCreateView(View):
    def get(self, req, *args, **kwargs):
        contexto = {'formulario': JogoModel2Form, }
        return render(req, "jogos/criaJogo.html", contexto)

    def post(self, req, *args, **kwargs):
        formulario = JogoModel2Form(req.POST)
        if formulario.is_valid():
            jogo = formulario.save()
            jogo.save()
            return HttpResponseRedirect(reverse_lazy("jogos:lista-jogos"))


class JogoUpdateView(View):
    def get(self, req, pk, *args, **kwargs):
        jogo = Jogo.objects.get(pk=pk)
        formulario = JogoModel2Form(instance=jogo)
        contexto = {'jogo': formulario}
        return render(req, 'jogos/atualizaJogo.html', contexto)

    def post(self, req, pk, *args, **kwargs):
        jogo = get_object_or_404(Jogo, pk=pk)
        formulario = JogoModel2Form(req.POST, instance=jogo)
        if formulario.is_valid():
            jogo = formulario.save()
            jogo.save()
            return HttpResponseRedirect(reverse_lazy('jogos:lista-jogos'))
        else:
            contexto = {'jogo': formulario}
            return render(req, 'jogos/atualizaJogo.html', contexto)


class JogoDeleteView(View):
    def get(self, req, pk, *args, **kwargs):
        jogo = Jogo.objects.get(pk=pk)
        contexto = {'jogo': jogo}
        return render(req, 'jogos/excluiJogo.html', contexto)

    def post(self, req, pk, *args, **kwargs):
        jogo = Jogo.objects.get(pk=pk)
        jogo.delete()
        return HttpResponseRedirect(reverse_lazy('jogos:lista-jogos'))
