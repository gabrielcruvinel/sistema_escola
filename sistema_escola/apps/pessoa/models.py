from django.db import models
from django.contrib.auth.models import User
from apps.endereco.models import Endereco

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    id_endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    nome = models.CharField(max_length=100, help_text='Nome', null=True)
    cpf = models.CharField(max_length=15, help_text='CPF', null=True)
    rg = models.CharField(max_length=10, help_text='RG', null=False)
    data_nascimento = models.DateField()

