from django.db import models

class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    desc_cargo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.desc_cargo
# Create your models here.
