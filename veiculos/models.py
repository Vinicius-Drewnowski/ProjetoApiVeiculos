from django.db import models
from django.contrib.auth.models import User

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    versao = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=30)
    placa = models.CharField(max_length=10)
    usuario = models.CharField(max_length=100)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"