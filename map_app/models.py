from django.db import models
from django.utils import timezone

class Orgao(models.Model):
    nome = models.CharField(max_length = 256)
    telefone = models.CharField(max_length = 32)
    email = models.EmailField(unique = True)
    site = models.URLField()

    #Coordenas geografica da sede do Orgao
    def __str__(self):
        return self.nome

class Despesa(models.Model):
    descricao = models.CharField(max_length = 256)
    valor = models.FloatField()
    data_inicio = models.DateField()
    data_update = models.DateField()
    # prazo em dias
    prazo = models.IntegerField(blank=True, null=True)

    # Coordenas geograficas da localizacao da obra0
    coordenadaS = models.FloatField()
    coordenadaW = models.FloatField()

    # Orgao resonsavel pela obra
    orgao = models.ForeignKey(Orgao, on_delete = models.CASCADE)

    def __str__(self):
        return self.descricao

# class Comentario(models.Model):
#     autor = models.CharField(max_lenght = 256)
#     data = models.DateTimeField()
#     texto = models.TextField()
#     orgao = models.ForeignKey(Orgao, on_delete = models.CASCADE)
