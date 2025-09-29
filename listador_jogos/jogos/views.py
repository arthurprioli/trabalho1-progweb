from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from jogos.models import Jogo, Avaliacao
from jogos.forms import JogoModel2Form, AvaliacaoModel2Form
from django.views.generic import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

class JogoAvaliacao(LoginRequiredMixin, View):
    def get(self,req,pk, *args, **kwargs):
        jogo = get_object_or_404(Jogo, pk=pk)
        avaliacoes = Avaliacao.objects.filter(jogo=jogo).order_by('-id')
        context = {
            'avaliacoes': avaliacoes,
            'jogo': jogo,
            "form": AvaliacaoModel2Form,
        }
        return render(req, 'jogos/listaAvaliacoes.html', context)
    def post(self, req, pk, *args, **kwargs):
        formulario = AvaliacaoModel2Form(req.POST)
        jogo = get_object_or_404(Jogo,pk=pk)
        avaliacoes = Avaliacao.objects.filter(jogo=jogo).order_by('-id')
        form = AvaliacaoModel2Form()
        if formulario.is_valid():
            avaliacao = formulario.save(commit=False)
            avaliacao.jogo = jogo
            avaliacao.autor = req.user
            avaliacao.save()
            avaliacoes = Avaliacao.objects.filter(jogo=jogo).order_by('-id')
            context = {
                "jogo": jogo,
                "avaliacoes": avaliacoes,
                "form": form,
            }
            return redirect(reverse("jogos:ve-avaliacao",kwargs ={"pk":jogo.id}))
        context = {
            "jogo": jogo,
            "avaliacoes": avaliacoes,
            "form": form,
        }
        return render(req, f'jogo/{jogo.id}/avaliacoes',context)
    