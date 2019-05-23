from django.db import models
'''

from django.contrib.auth.models import User

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    #id_endereco = models.ForeignKey(Endereco)
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    nome = models.CharField(max_length=100, help_text='Nome', blank=True)
    cpf = models.CharField(max_length=15, help_text='CPF', blank=True)
    rg = models.CharField(max_length=10, help_text='RG', blank=False)
    data_nascimento = models.DateField()
    
'''