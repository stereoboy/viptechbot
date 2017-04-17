from django.conf.urls import url

from .import views
from django.views.decorators.csrf import csrf_exempt, csrf_protect

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^me$', views.me),
  url(r'^updates$', views.updates),
  url(r'^getwebhookinfo$', views.getwebhookinfo),
  url(r'^setwebhook$', views.setwebhook),
  url(r'^resetwebhook$', views.resetwebhook),
  #url(r'^webhook/(?P<token>[-_:a-zA-Z0-9]+)/$', csrf_exempt(views.webhook)),
  url(r'^webhook$', csrf_exempt(views.webhook)), #telegram does not use csrf
]
