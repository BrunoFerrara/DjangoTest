from datetime import datetime

from django.http import HttpResponse

from django.shortcuts import render

def saludar(request):
    saludo = "Hola querido usuario"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

