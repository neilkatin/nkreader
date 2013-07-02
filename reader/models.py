from django.db import models

# Create your models here.
class TwitterUser(models.Model):
    user_name = models.CharField('user name', max_length=200)
    cauth = models.CharField('callback temp auth token', max_length=200, blank=True)
    cauth_secret = models.CharField('callback temp auth token', max_length=200, blank=True)
    auth = models.CharField('access token', max_length=200, blank=True)
    auth_secret = models.CharField('access auth secret', max_length=200, blank=True)

    def __unicode__(self):
        return self.user_name

class TwitterApp(models.Model):
    name = models.CharField('descriptive name for app', max_length=128, unique=True)
    consumer_key = models.CharField('app consumer key', max_length=128, unique=True)
    consumer_secret = models.CharField('app consumer secret', max_length=128)

    def __unicode__(self):
        return ("%s/%s") % (self.name, self.consumer_key)

