from rest_framework import serializers
from .models import Agendamento, Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['number', 'name', 'email']

class AgendamentoSerializer(serializers.ModelSerializer):

    # Formato de entrada para a data
    date = serializers.DateTimeField(input_formats=['%d/%m/%Y %H:%M', '%Y-%m-%dT%H:%M:%S'])
    
    class Meta:
        model = Agendamento
        fields = ['user', 'date', 'service']
        # Define os campos que serão serializados/deserializados