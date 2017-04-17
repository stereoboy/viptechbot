import urllib.request
import urllib.parse
import urllib.error
from django.http import HttpResponse
import logging
import infos
import json
import re

#
# reference : http://bakyeono.net/post/2015-08-24-using-telegram-bot-api.html#2-%EB%B4%87%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%84%9C%EB%B2%84-%EC%A4%80%EB%B9%84
#

# setup logger
logger = logging.getLogger('telegramapi')
# remove local setup, follow default setting
#logger.setLevel(logging.INFO)
#hdlr = logging.FileHandler(infos.LOG_DIR + 'telegram.log')
#hdlr = logging.StreamHandler()
#hdlr.setLevel(logging.INFO)
#formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
#hdlr.setFormatter(formatter)
#logger.addHandler(hdlr)

logger.info("setup done")

# setup variable
TOKEN = infos.TOKEN
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

CMD_START     = '/start'
CMD_STOP      = '/stop'
CMD_HELP      = '/help'
CMD_BROADCAST = '/broadcast'

USAGE = u"""[usage]
/start - ()
/stop  - ()
/help  - ()
"""
MSG_START = u'bot get started.'
MSG_STOP  = u'bot is stopped'

CUSTOM_KEYBOARD = [
    [CMD_START],
    [CMD_STOP],
    [CMD_HELP],
    ]

# 채팅별 봇 활성화 상태
# 구글 앱 엔진의 Datastore(NDB)에 상태를 저장하고 읽음
# 사용자가 /start 누르면 활성화
# 사용자가 /stop  누르면 비활성화
#class EnableStatus(ndb.Model):
#  enabled = ndb.BooleanProperty(required=True, indexed=True, default=False,)

class Connection():
  def __init__(self, chat_id):
    self.chat_id = chat_id

def set_enabled(chat_id, enabled):
  u"""set_enabled: 봇 활성화/비활성화 상태 변경
  chat_id:    (integer) 봇을 활성화/비활성화할 채팅 ID
  enabled:    (boolean) 지정할 활성화/비활성화 상태
  """
#  es = EnableStatus.get_or_insert(str(chat_id))
#  es.enabled = enabled
#  es.put()
  pass

def get_enabled(chat_id):
  u"""get_enabled: 봇 활성화/비활성화 상태 반환
  return: (boolean)
  """
#  es = EnableStatus.get_by_id(str(chat_id))
#  if es:
#    return es.enabled
#  return False
  return True

def get_enabled_chats():
  u"""get_enabled: 봇이 활성화된 채팅 리스트 반환
  return: (list of EnableStatus)
  """
#  query = EnableStatus.query(EnableStatus.enabled == True)
#  return query.fetch()
  return []

# 메시지 발송 관련 함수들
def send_msg(chat_id, text, reply_to=None, no_preview=True, keyboard=None):
  u"""send_msg: 메시지 발송
  chat_id:    (integer) 메시지를 보낼 채팅 ID
  text:       (string)  메시지 내용
  reply_to:   (integer) ~메시지에 대한 답장
  no_preview: (boolean) URL 자동 링크(미리보기) 끄기
  keyboard:   (list)    커스텀 키보드 지정
  """
  params = {
      'chat_id': str(chat_id),
      'text': text.encode('utf-8'),
      }
  if reply_to:
    params['reply_to_message_id'] = reply_to
  if no_preview:
    params['disable_web_page_preview'] = no_preview
  if keyboard:
    reply_markup = json.dumps({
      'keyboard': keyboard,
      'resize_keyboard': True,
      'one_time_keyboard': False,
      'selective': (reply_to != None),
      })
    params['reply_markup'] = reply_markup

  try:
    msg = urllib.parse.urlencode(params)
    logger.info('sendmessage(' + msg + ")")
    encoded_msg = msg.encode('utf-8')
    urllib.request.urlopen(BASE_URL + 'sendMessage', encoded_msg)
  except Exception as e:
    logger.exception(e)

def broadcast(text):
  u"""broadcast: 봇이 켜져 있는 모든 채팅에 메시지 발송
  text:       (string)  메시지 내용
  """
  for chat in get_enabled_chats():
    send_msg(chat.key.string_id(), text)

# 봇 명령 처리 함수들
def cmd_start(chat_id):
  u"""cmd_start: 봇을 활성화하고, 활성화 메시지 발송
  chat_id: (integer) 채팅 ID
  """
  set_enabled(chat_id, True)
  send_msg(chat_id, MSG_START, keyboard=CUSTOM_KEYBOARD)

def cmd_stop(chat_id):
  u"""cmd_stop: 봇을 비활성화하고, 비활성화 메시지 발송
  chat_id: (integer) 채팅 ID
  """
  set_enabled(chat_id, False)
  send_msg(chat_id, MSG_STOP)

def cmd_help(chat_id):
  u"""cmd_help: 봇 사용법 메시지 발송
  chat_id: (integer) 채팅 ID
  """
  send_msg(chat_id, USAGE, keyboard=CUSTOM_KEYBOARD)

def cmd_broadcast(chat_id, text):
  u"""cmd_broadcast: 봇이 활성화된 모든 채팅에 메시지 방송
  chat_id: (integer) 채팅 ID
  text:    (string)  방송할 메시지
  """
  send_msg(chat_id, u'메시지를 방송합니다.', keyboard=CUSTOM_KEYBOARD)
  broadcast(text)

def cmd_echo(chat_id, text, reply_to):
  u"""cmd_echo: 사용자의 메시지를 따라서 답장
  chat_id:  (integer) 채팅 ID
  text:     (string)  사용자가 보낸 메시지 내용
  reply_to: (integer) 답장할 메시지 ID
  """
  send_msg(chat_id, text, reply_to=reply_to)

def process_cmds(msg):
  u"""사용자 메시지를 분석해 봇 명령을 처리
  chat_id: (integer) 채팅 ID
  text:    (string)  사용자가 보낸 메시지 내용
  """
  msg_id = msg['message_id']
  chat_id = msg['chat']['id']
  text = msg.get('text')
  if (not text):
    return
  if CMD_START == text:
    cmd_start(chat_id)
    return
  if (not get_enabled(chat_id)):
    return
  if CMD_STOP == text:
    cmd_stop(chat_id)
    return
  if CMD_HELP == text:
    cmd_help(chat_id)
    return
  cmd_broadcast_match = re.match('^' + CMD_BROADCAST + ' (.*)', text)
  if cmd_broadcast_match:
    cmd_broadcast(chat_id, cmd_broadcast_match.group(1))
    return
  cmd_echo(chat_id, text, reply_to=msg_id)
  return

def get_json_from_url(url, data=None):
  json_data=None
  try:
    fp= urllib.request.urlopen(url, data)
    data = fp.read()
    http_info = fp.info()
    encoding = http_info.get_content_charset('utf-8')
    json_data = json.loads(data.decode(encoding))
  except urllib.error.HTTPError as e:
    logger.exception(e)
    logger.exception(e.read())
  return json_data

def me():
  url = BASE_URL + 'getMe'
  json_data = get_json_from_url(url)
  return HttpResponse( json.dumps(json_data),
      content_type="application/json")

def updates():
  url = BASE_URL + 'getUpdates'
  json_data = get_json_from_url(url)
  return HttpResponse( json.dumps(json_data),
      content_type="application/json")

def getwebhookinfo():
  url = BASE_URL + 'getWebhookInfo'
  json_data = get_json_from_url(url)
  logger.info("getWebhookInfo return:" + json.dumps(json_data))
  return HttpResponse( json.dumps(json_data),
      content_type="application/json")

def setwebhook():
  logger.info("setwebhook()")
  url = BASE_URL + 'setWebhook'
  #target_url = "http://" + infos.HOST + ":8000" + "/webhook"
  target_url = "https://" + infos.HOST + "/telegrambot/webhook"
  data = urllib.parse.urlencode({'url': target_url})
  logger.info("data:" + data)
  data = data.encode('utf-8')
  logger.info("url:" + url)

  json_data = get_json_from_url(url, data)
  logger.info("setWebhook return:" + json.dumps(json_data))
  return HttpResponse(
      json.dumps(json_data),
      content_type="application/json")

def resetwebhook():
  logger.info("resetwebhook()")
 
  ret = {}
  url = BASE_URL + 'deleteWebhook'
  json_data = get_json_from_url(url)
  ret['deleteWebhook'] = json_data
  
  url = BASE_URL + 'setWebhook'
  #target_url = "http://" + infos.HOST + ":8000" + "/telegrambot/webhook"
  target_url = "https://" + infos.HOST + "/telegrambot/webhook"
  data = urllib.parse.urlencode({'url': target_url})
  logger.info("data:" + data)
  data = data.encode('utf-8')
  logger.info("url:" + url)

  json_data = get_json_from_url(url, data)
  ret['setWebhook'] = json_data
  logger.info("setWebhook return:" + json.dumps(ret))
  return HttpResponse(
      json.dumps(ret),
      content_type="application/json")

def webhook(request):
  #logger.info("webhook() token:" + token)
  json_data = request.body.decode('utf-8')
  logger.info("webhook() request.body=" + json_data)
  body = json.loads(json_data)
  #logger.info("setWebhook return:" + json.dumps(body))
  #self.response.write(json.dumps(body))
  process_cmds(body['message'])
  return HttpResponse(
      json.dumps(body),
      content_type="application/json")
