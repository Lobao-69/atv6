from django.db import models

# Create your models here.
class Disco(models.Model):
    nome_text = models.CharField(max_length= 255)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length= 255)
    ano = models.PositiveIntegerField()
    pais = models.CharField(max_length= 255)
    genero = models.CharField(max_length= 255)
    quantidade = models.PositiveIntegerField()
