from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Itens (models.Model):
    chave = 'CH'
    cracha = 'CR'
    folha = 'FO'

    Tipos_de_itens = [
        (chave, 'Chave'),
        (cracha, 'Cracha'),
        (folha, 'Folha'),
    ]

    tipo = models.CharField(
        max_length=2,
        choices= Tipos_de_itens,
        default= chave,
    )
    descricao = models.TextField(blank=True, null= True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tipo
    