from django.shortcuts import render

import kakaobot.kakaoapi as kakaoapi

# Create your views here.

def index(request):
  if request.method == 'GET':
    return HttpResponse("Welcome!")

def keyboard(request):
  if request.method == 'GET':
    return kakaoapi.keyboard(request)

def message(request):
  if request.method == 'POST':
    return kakaoapi.message(request)

def friend_post(request):
  if request.method == 'POST':
    return kakaoapi.friend_post(request)

def friend_delete(request, user_key):
  print(user_key)
  if request.method == 'DELETE':
    return kakaoapi.friend_delete(request, user_key)

def chat_room(request, user_key):
  print(user_key)
  if request.method == 'DELETE':
    return kakaoapi.chat_room(request)
