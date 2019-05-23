from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Escola')
