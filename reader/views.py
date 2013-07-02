# Create your views here.
from django.http import HttpResponse
#from django.template import RequestContext, loader
from django.shortcuts import render

from reader.twapi import Twapi

def index(request):
    return HttpResponse("Hello word: user index")

def getToken(request, user_name):

    twapi = Twapi()
    auth = twapi.getAccessToken(user_name)

    return HttpResponse("auth.oauth_token %s auth.oauth_token_secret %s auth.auth_url %s" % (auth["oauth_token"], auth["oauth_token_secret"], auth["auth_url"]))


def recordToken(request, user_name, verifier):
    twapi = Twapi()
    twapi.recordToken(user_name, verifier)

    return HttpResponse("Recorded...")

def timeline(request, user_name):
    twapi = Twapi()
    tl = twapi.getTimeline(user_name)
    context = { 'user_name': user_name, 'tweet_list': tl }
    return render(request, 'reader/tweetlist.html', context)

