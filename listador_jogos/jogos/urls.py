from django.urls import path
from jogos import views

app_name = "jogos"

urlpatterns = [
    path('listaJogos', views.JogoListView.as_view(), name='lista-jogos'),
    path('criaJogo', views.JogoCreateView.as_view(), name='cria-jogo'),
    path('atualizaJogo/<int:pk>',
         views.JogoUpdateView.as_view(), name='atualiza-jogo'),
    path('excluiJogo/<int:pk>',
         views.JogoDeleteView.as_view(), name='delete-jogo'),
    path('', views.JogoListView.as_view(), name='home-jogos'),
    path('seguranca/', views.segurancahome, name='segurancahome'),
    path('seguranca/register', views.register, name='register'),
]
