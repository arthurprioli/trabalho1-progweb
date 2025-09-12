from django import forms
from jogos.models import Jogo
from datetime import datetime


class JogoModel2Form(forms.ModelForm):
    anoJogo = forms.IntegerField(min_value=1900, max_value=datetime.now().year,
                                 label='Ano de lançamento do jogo',
                                 help_text='Ano de lançamento do jogo')

    class Meta:
        model = Jogo
        fields = '__all__'
