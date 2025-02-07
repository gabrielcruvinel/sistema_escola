from django.db import models

class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    cep = models.CharField(max_length=15, help_text='CEP', blank=True)
    bairro = models.CharField(max_length=50, help_text='Bairro')
    cidade = models.CharField(max_length=50, help_text='Cidade')
    uf = models.CharField(max_length=10, help_text='Estado')

    def __str__(self):
        return self.cep, self.cidade