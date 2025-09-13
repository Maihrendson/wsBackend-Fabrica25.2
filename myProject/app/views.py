from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer

import json

@api_view(['GET'])
def listar_usuarios(request):

    # Lista todos os usuários cadastrados
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_usuario(request):
    
    # Cria um novo usuário
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def obter_usuario(request, number):

    # Obtém detalhes de um usuário pelo número
    try:
        usuario = Usuario.objects.get(number=number)
    except Usuario.DoesNotExist:
        return Response({'erro': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizar_usuario(request, number):

    # Atualiza dados de um usuário existente
    try:
        usuario = Usuario.objects.get(number=number)
    except Usuario.DoesNotExist:
        return Response({'erro': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_usuario(request, number):

    # Remove um usuário do sistema
    try:
        usuario = Usuario.objects.get(number=number)
    except Usuario.DoesNotExist:
        return Response({'erro': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    usuario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)