
from twython import Twython
from reader.models import TwitterApp, TwitterUser

APP_NAME = 'nkreader';

class Twapi:

    def __init__(self):
        self.appObj = TwitterApp.objects.get(name=APP_NAME)

    def getAccessToken(self, user_name):
        twython = Twython(self.appObj.consumer_key, self.appObj.consumer_secret)
        auth = twython.get_authentication_tokens()

        tusers = TwitterUser.objects.filter(user_name=user_name)

        if tusers:
            # fetch the existing user
            tuser = tusers[0]
        else:
            # create the user
            tuser = TwitterUser(user_name=user_name)

        tuser.cauth = auth['oauth_token']
        tuser.cauth_secret = auth['oauth_token_secret']
        tuser.auth = tuser.auth_secret = ""
        tuser.save()

        return auth

    def recordToken(self, user_name, verifier):

        tuser = TwitterUser.objects.get(user_name=user_name)

        twython = Twython(self.appObj.consumer_key, self.appObj.consumer_secret, tuser.cauth, tuser.cauth_secret)
        final_step = twython.get_authorized_tokens(verifier)

        tuser.cauth = tuser.cauth_secret = ""
        tuser.auth = final_step['oauth_token']
        tuser.auth_secret = final_step['oauth_token_secret']
        tuser.save()

    def getTimeline(self, user_name):
        tuser = TwitterUser.objects.get(user_name=user_name)
        twython = Twython(self.appObj.consumer_key, self.appObj.consumer_secret, tuser.auth, tuser.auth_secret)

        return twython.get_home_timeline()
