from django import forms
from jogos.models import Jogo
from datetime import datetime


class JogoModel2Form(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'ano', 'capa', 'empresa']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-0',
                'placeholder': 'Ex: GTA V'
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light border-0',
                'placeholder': 'Ex: 2013'
            }),
            'capa': forms.URLInput(attrs={
                'class': 'form-control bg-dark text-light border-0',
                'placeholder': 'URL da capa do jogo'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-0',
                'placeholder': 'Ex: Rockstar Games'
            }),
        }
