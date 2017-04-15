from django.shortcuts import render

from django.http import HttpResponse
import json
import urllib
import telegrambot.telegramapi as telegramapi
import infos
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

def webhook(request):
  print("webhook")
  if request.method == 'POST':
    print("webhookPOST")
    return telegramapi.webhook(request)
