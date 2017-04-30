from django.contrib import admin

from .models import User, TextMessage, Image, Message
# Register your models here.
admin.site.register(User)
admin.site.register(TextMessage)
admin.site.register(Image)
admin.site.register(Message)
