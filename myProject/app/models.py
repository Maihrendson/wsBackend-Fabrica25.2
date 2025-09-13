from django.db import models

class Usuario(models.Model):
        #Cria número da Tabela usuário
    number = models.CharField(max_length=13, primary_key=True, default= '')
        #Cria nome da Tabela usuário
    name = models.CharField(max_length=255, default= '')
        #Cria email da Tabela usuário
    email = models.CharField(max_length=100, default= '')

    #Define como o objeto será representado como string no Django
    def __str__(self):
        return f"Nome: {self.name} | Email: {self.email} | Número: {self.number}"

