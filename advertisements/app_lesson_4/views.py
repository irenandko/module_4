from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Домашка к 4 занятию')

# Create your views here.
