from django.db import models
from django.utils import timezone

class Localizacao(models.Model):
    estado = models.CharField(max_length = 2)
    cidade = models.CharField(max_length = 50)
    bairro = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 256)
    cep = models.CharField(max_length = 8)

    latitude = models.DecimalField(null = False)
    longitude = models.DecimalField(null = False)
    def __str__(self):
        str = self.estado + ', ' + self.cidade +', ' + self.bairro
        if self.endereco != '':
            str += ', ' + self.endereco
        return str


class Instituicao(models.Model):
    nome = models.CharField(max_length = 256)
    telefone = models.CharField(max_length = 32)
    email = models.EmailField()
    site = models.URLField()
    localizacao = models.ForeignKey(Localizacao, on_delete = models.SET_NULL, null = True)
    def __str__(self):
        return self.nome

class Orgao(models.Model):
    nome = models.CharField(max_length = 256)
    telefone = models.CharField(max_length = 32)
    email = models.EmailField()
    site = models.URLField()
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE)
    localizacao = models.ForeignKey(Localizacao, on_delete = models.SET_NULL, null = True)
    def __str__(self):
        return self.nome

class Despesa(models.Model):
    descricao = models.CharField(max_length = 256)

    empenhado = models.DecimalField()
    anulado = models.DecimalField()
    liquidado = models.DecimalField()
    pago = models.DecimalField()

    data_inicio = models.DateField()
    data_update = models.DateField()

    localizacao = models.ForeignKey(Localizacao, on_delete = models.SET_NULL, null = True)

    # Orgao resonsavel pela obra
    orgao = models.ForeignKey(Orgao, on_delete = models.CASCADE)
    def __str__(self):
        return self.descricao
