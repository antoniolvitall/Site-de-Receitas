from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('home 2')


def contato(request):
    return HttpResponse('contato2')


def sobre(request):
    return HttpResponse('sobre2')
