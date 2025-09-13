from django.db import models

class Usuario(models.Model):
        #Cria número da Tabela usuário
    number = models.CharField(max_length=11, primary_key=True, default= '')
        #Cria nome da Tabela usuário
    name = models.CharField(max_length=255, default= '')
        #Cria email da Tabela usuário
    email = models.CharField(max_length=100, default= '')

    #Define como o objeto será representado como string no Django
    def __str__(self):
        return f"Nome: {self.name} | Email: {self.email} | Número: {self.number}"
    
class Agendamento(models.Model):

    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='agendamentos')
    date = models.DateTimeField()
    service = models.CharField(max_length=100)

    def __str__(self):
        return f" Cliente: {self.user.name} | Data: {self.date} | Serviço: {self.service}"
