from django.db import models

class Pessoa(models.Model0):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Nome', blank=False)
    cpf = models.CharField(max_length=15, help_text='CPF', blank=False)
    rg = models.CharField(max_length=10, help_text='RG', blank=True)
    data_nascimento = models.DateField()


