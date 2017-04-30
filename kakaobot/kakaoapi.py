import urllib.request
import urllib.parse
import urllib.error
from django.http import HttpResponse
from django.core.files import File
import logging
import infos
import json
import os
import re

from common.models import User, TextMessage, Image, Message
# setup logger
logger = logging.getLogger('kakaoapi')
logger.info("telegrambot setup done")

def read_file_from_url(url):
  try:
    f = urllib.request.urlopen(url)
    logger.info("downloading from " + url + " ...")
    return f
  except urllib.HTTPError as e:
    logger.exception(url)
    logger.exception(e)
    logger.exception(e.read())
  except urllib.URLError as e:
    logger.exception(url)
    logger.exception(e)
    logger.exception(e.read())

def keyboard(request):
  logger.info("request")
  json_data = {
      "type" : "buttons",
      "buttons" : ["Option 1", "Option 2", "Option 3"]
      }
  return HttpResponse(json.dumps(json_data),
      content_type="application/json")


def save_message(msg):
  user_id = "kakao_" + str(msg['user_key'])
  if User.objects.filter(user_id=user_id).exists():
    user = User.objects.get(user_id=user_id)
    logger.info("This user is already registered:" + user_id)
  else:
    first_name =''
    last_name = ''
    nick_name = ''
    user = User.objects.create(user_id=user_id, first_name=first_name, last_name=last_name, nick_name=nick_name)

  message = Message(user=user)

  if msg['type'] == 'text':
    text = TextMessage.objects.create(text=msg['content'])
    message.text = text
  if msg['type'] == 'photo':
    photo_url = msg['content']
    f = read_file_from_url(photo_url)
    photo = Image()

    image_file = File(f)
    photo.image.save(os.path.basename(photo_url), image_file)
    message.image = photo

  message.save()

def message(request):
  logger.info("message")
  data = request.body.decode('utf-8')
  json_data = json.loads(data)
  logger.info("message() request.body=" + data)
  logger.info(request)

  save_message(json_data)

  json_data = {
      "message":{
        "text" : json_data['content']
        }
      }
  return HttpResponse(json.dumps(json_data),
      content_type="application/json")

def friend_post(request):
  logger.info("friend_post")
  json_data = request.body.decode('utf-8')
  logger.info("friend_post() request.body=" + json_data)
  logger.info(request)
  json_data ={
      "code": 0,
      "message": "SUCCESS",
      "comment": "정상 응답"
      }
  return HttpResponse(json.dumps(json_data), status=200,
      content_type="application/json")

def friend_delete(request, user_key):
  json_data ={ 
      "code": 0,
      "message": "SUCCESS",
      "comment": "정상 응답"
      }
  return HttpResponse(json.dumps(json_data), status=200,
      content_type="application/json")

def chat_room(request):
  json_data ={ 
      "code": 0,
      "message": "SUCCESS",
      "comment": "정상 응답"
      }
  return HttpResponse(json.dumps(json_data), status=200,
      content_type="application/json")
