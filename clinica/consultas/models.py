from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=50)

    hora_inicio = models.TimeField(default='08:00')
    hora_final = models.TimeField(default='18:00')

    def __str__(self):
        return f'{self.nome} - {self.especialidade}'

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    hora_consulta = models.TimeField()

    def __str__(self):
        return f'{self.paciente} - {self.medico} em {self.data_consulta} às {self.hora_consulta}'
