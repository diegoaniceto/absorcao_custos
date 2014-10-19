from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.nome
