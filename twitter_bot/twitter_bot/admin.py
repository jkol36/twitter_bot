from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(TwitterUser)
admin.site.register(TwitterStatus)
admin.site.register(hashtag)
admin.site.register(OauthSet)
