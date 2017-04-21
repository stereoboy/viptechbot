from django.conf.urls import url

from .import views
from django.views.decorators.csrf import csrf_exempt, csrf_protect

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^keyboard$', views.keyboard),
  url(r'^message$', csrf_exempt(views.message)),
  url(r'^friend$', csrf_exempt(views.friend_post)),
  url(r'^friend/(?P<user_key>.+)$', csrf_exempt(views.friend_delete)),
  url(r'^chat_room/(?P<user_key>.+)$', csrf_exempt(views.chat_room)),
]
