from django.db import models
from apps.pessoa.models import Pessoa
from apps.cargo.models import Cargo
# Create your models here.
class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    salario = models.FloatField()
    hora_extra = models.BigIntegerField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True)