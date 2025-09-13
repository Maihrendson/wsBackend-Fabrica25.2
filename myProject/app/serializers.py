from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['number', 'name', 'email']
        # Define os campos que serão serializados/deserializados