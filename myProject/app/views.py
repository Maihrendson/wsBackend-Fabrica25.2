from django.shortcuts import rende
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from serializers import UsuarioSerializer

import json

# Create your views here.
