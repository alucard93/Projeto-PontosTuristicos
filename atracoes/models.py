from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descrição = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self) -> str:
        return self.nome