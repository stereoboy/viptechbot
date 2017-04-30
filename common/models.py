from django.db import models
import datetime

# Create your models here.
class User(models.Model):
  user_id = models.CharField(max_length=256, default='')
  first_name = models.CharField(max_length=256, default='')
  last_name = models.CharField(max_length=256, default='')
  nick_name = models.CharField(max_length=256, default='')
  def __str__(self):
    return str(self.user_id) + ':' + str(self.first_name) + ' ' + str(self.last_name) + '(' + str(self.nick_name) + ')'

class TextMessage(models.Model):
  text = models.TextField()
  label = models.CharField(max_length=256, default='')
  def __str__(self):
    return self.text

class Image(models.Model):
  image = models.ImageField(upload_to='./')
  label = models.CharField(max_length=256, default='')
  def __str__(self):
    return self.image.name

class Message(models.Model):
  date = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User)
  #to = models.ForeignKey(User, default=None)
  text = models.ForeignKey(TextMessage, models.SET_NULL, blank=True, null=True)
  image = models.ForeignKey(Image, models.SET_NULL, blank=True, null=True)
  def __str__(self):
    return str(self.date) + ':' + str(self.text)[:100]
