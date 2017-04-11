from django.shortcuts import render

from django.http import HttpResponse
import json
import urllib
import telegrambot.telegramapi
import infos
# Create your views here.

TOKEN = infos.TOKEN
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def index(request):
  if request.method == 'GET':
    return HttpResponse("Welcome!")

def me(request):
  if request.method == 'GET':
    return telegramapi.me()


def updates(request):
  if request.method == 'GET':
    return HttpResponse("updates handler")


def setwebhook(request):
  if request.method == 'GET':
    url = request.GET.get('url')
    return telegramapi.setwebhook(url)

def webhook(request):
  if request.method == 'POST':
    return telegramapi.webhook(request)
