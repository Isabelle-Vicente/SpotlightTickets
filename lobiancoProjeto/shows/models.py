from django.db import models

class Show(models.Model):
    TIPO_CHOICES = (
        ('Comedia', 'Comédia'),
        ('Acao', 'Ação'),
        ('Drama', 'Drama'),
    )

    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES) 
    assentos = models.IntegerField()
    elenco = models.CharField(max_length=200)
    secoes = models.IntegerField()
    data = models.DateField()
    horarios = models.TimeField()

    def __str__(self):
        return self.nome