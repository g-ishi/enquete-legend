from django.contrib import admin

from .models import FriendModel
from .models import MessageModel


# Register your models here.
admin.site.register(FriendModel)
admin.site.register(MessageModel)
