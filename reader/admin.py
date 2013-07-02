from django.contrib import admin
from reader.models import TwitterUser
from reader.models import TwitterApp

admin.site.register(TwitterUser)
admin.site.register(TwitterApp)
