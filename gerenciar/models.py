from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    situacao = models.CharField(max_length=10, choices=[('ativa', 'Ativa'), ('inativa', 'Inativa')])

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_termino = models.TimeField()

    def __str__(self):
        return f"{self.sala.nome} - {self.data}"


# Create your models here.


