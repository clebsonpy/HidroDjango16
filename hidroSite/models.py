from django.db import models

# Create your models here.
class TipoDados(models.Model):
    tipoDadosID = models.AutoField(primary_key=True, null=False)
    tipoDados = models.CharField(max_length=25, null=False)

class Reducao(models.Model):
    reducaoID = models.AutoField(primary_key=True, null=False)
    tipoReducao = models.CharField(max_length=20, null=False)

class TesteAderencia(models.Model):
    testeAderenciaID = models.AutoField(primary_key=True, null=False)
    tipoTeste = models.CharField(max_length=50, null=False)

class Estimadores(models.Model):
    estimadorID = models.AutoField(primary_key=True, null=False)
    metodo = models.CharField(max_length=50, null=False)

class Distribuicoes(models.Model):
    distribuicaoID = models.AutoField(primary_key=True, null=False)
    distribuicao = models.CharField(max_length=50, null=False)

class SerieExtensa(models.Model):
    serieExtensaID = models.AutoField(primary_key=True, null=False)
    tipoDadosID = models.ForeignKey(TipoDados, null=False)
    reducaoID = models.ForeignKey(Reducao, null=False)
    dados = models.FloatField(null=False)

class SerieReamostragem(models.Model):
    serieReamostragemID = models.AutoField(primary_key=True, null=False)
    serieExtensaID = models.ForeignKey(SerieExtensa, null=False)
    tamanho = models.IntegerField(null=False)
    ordem = models.IntegerField(null=False)

class Parametros(models.Model):
    parametrosID = models.AutoField(primary_key=True, null=False)
    ordem = models.IntegerField(null=False)
    tamanho = models.IntegerField(null=False)
    estimadorID = models.ForeignKey(Estimadores, null=False)
    distribuicaoID = models.ForeignKey(Distribuicoes, null=False)
    forma = models.FloatField(null=False)
    escala = models.FloatField(null=False)
    posicao = models.FloatField(null=False)

class Qualidade(models.Model):
    qualidadeID = models.AutoField(primary_key=True, null=False)
    testeAderenciaID = models.ForeignKey(TesteAderencia, null=False)
    parametrosID = models.ForeignKey(Parametros, null=False)
    estatisticaTeste = models.FloatField(null=False)
    valorP = models.FloatField(null=False)
    h = models.IntegerField(null=False)
