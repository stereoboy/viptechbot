from django.shortcuts import render

from django.http import HttpResponse
import json
import urllib
# Create your views here.

TOKEN = '270279298:AAFD3QcN5w3txqHj61K47CJhQ2dWrLNQ19k'
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def index(request):
  if request.type == 'GET':
    return HttpResponse("Welcome!")

def me(request):
  if request.type == 'GET':
    return HttpResponse("me handler")


def updates(request):
  if request.type == 'GET':
    return HttpResponse("updates handler")


def setwebhook(request):
  if request.type == 'GET':
    url=request.url
    ret = json.load(urllib.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))
    return HttpResponse(
        json.dumps(ret),
        content_type="application/json")

def webhook(request):
  if request.type == 'POST':
    return HttpREsponse("webhook handler")
