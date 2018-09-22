from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Orgao(models.Model):
    nome = models.CharField(max_length = 256, unique = True)
    telefone = models.CharField(max_length = 32, unique = True)
    email = models.EmailField(unique = True)

    #Coordenas geografica da sede do Orgao
    coordenadaS = models.FloatField()
    coordenadaW = models.FloatField()
    def __str__(self):
        return self.nome

class Obra(models.Model):
    descricao = models.CharField(max_length = 256)
    valor = models.FloatField()
    data_inicio = models.DateField()
    data_update = models.DateField()
    # prazo em dias
    prazo = models.IntegerField()

    # Coordenas geograficas da localizacao da obra0
    coordenadaS = models.FloatField()
    coordenadaW = models.FloatField()

    # Orgao resonsavel pela obra
    orgao = models.ForeignKey(Orgao, on_delete = models.CASCADE)

    def __str__(self):
        return self.descricao
