import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

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
    imagem = models.ImageField(upload_to='shows/')

    def __str__(self):
        return self.nome
    
@receiver(post_delete, sender=Show)
def delete_show_image(sender, instance, **kwargs):
    if instance.imagem:
        if os.path.isfile(instance.imagem.path):
            os.remove(instance.imagem.path)