from django.conf.urls import url

from .import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^me$', views.me),
  url(r'^updates$', views.updates),
  url(r'^set-webhook$', views.setwebhook),
  url(r'^webhook$', views.webhook),
] 
