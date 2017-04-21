import urllib.request
import urllib.parse
import urllib.error
from django.http import HttpResponse
import logging
import infos
import json
import re

# setup logger
logger = logging.getLogger('kakaoapi')
logger.info("telegrambot setup done")

def keyboard(request):
  logger.info("request")
  json_data = {
      "type" : "buttons",
      "buttons" : ["Option 1", "Option 2", "Option 3"]
      }
  return HttpResponse(json.dumps(json_data),
      content_type="application/json")

def message(request):
  logger.info("message")
  json_data = request.body.decode('utf-8')
  logger.info("message() request.body=" + json_data)
  logger.info(request)
  json_data = {
      "message":{
        "text" : "귀하의 차량이 성공적으로 등록되었습니다. 축하합니다!"
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
