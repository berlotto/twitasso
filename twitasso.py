# -*- encoding: utf-8 -*-

from twython import Twython
import time
import webbrowser as browser
import threading

APP_KEY = "<YOUR_APP_KEY>"
APP_SECRET = "<YOUR_APP_KEY_SECRET>"
TIME = 60 #In seconds

t = Twython(APP_KEY, APP_SECRET)

auth = t.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

browser.open(auth['auth_url'])

print "If your browser not open, then open a new tab and navigate to: %s" % auth['auth_url']

THE_PIN = raw_input("Write the PIN returned in your browser:")

twitter = Twython(APP_KEY, APP_SECRET,
					OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(THE_PIN)

FINAL_OAUTH_TOKEN = final_step['oauth_token']
FINAL_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)

credencials = twitter.verify_credentials()

print "Hello %s! You are '%s' in Twitter, and now I'll twiit for you..." % (credencials['name'], credencials['screen_name'])

try:
    f = open('twits.txt')
    for line in f:
    	print "Twitando: %s" % line
        twitter.update_status(status=line)
        time.sleep(TIME)
except TwythonError as e:
    print e

print "Concluído!"