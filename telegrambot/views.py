from django.shortcuts import render

from django.http import HttpResponse
import json
import urllib
import telegrambot.telegramapi as telegramapi
import infos
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

def index(request):
  if request.method == 'GET':
    return HttpResponse("Welcome!")

def me(request):
  if request.method == 'GET':
    return telegramapi.me()


def updates(request):
  if request.method == 'GET':
    return HttpResponse("updates handler")

def getwebhookinfo(request):
  if request.method == 'GET':
    return telegramapi.getwebhookinfo()

def setwebhook(request):
  if request.method == 'GET':
    #url = request.GET.get('url')
    return telegramapi.setwebhook()

def resetwebhook(request):
  if request.method == 'GET':
    #url = request.GET.get('url')
    return telegramapi.resetwebhook()

def webhook(request):
  if request.method == 'POST':
    return telegramapi.webhook(request)
