from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Create your models here.


class Jogo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=256, help_text='Insira o nome do jogo')
    ano = models.IntegerField(help_text='Insira o ano do jogo',
                              validators=[
                                  MinValueValidator(1900),
                                  MaxValueValidator(datetime.now().year)
                              ])
    
    capa = models.CharField(
        max_length=256, help_text="Insira a capa do jogo"
    )
    
    empresa = models.CharField(
        max_length=256, help_text='Insira o nome da empresa')

    def __str__(self):
        return self.nome
