from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    publicado = models.BooleanField(default=False)
    autor = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
