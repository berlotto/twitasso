from twython import Twython
import time

tempo = 60
app_key = "5Llo6LA1DldnAdUrgAF5A"
app_secret = "Bvh8NlRXpWZz3ZsOcUelGOznm3afectdMJ1Wgkk"
oauth_token = "22940852-NDwTnkRe7itGdhEHWFT5CuAFbQm3tcjc5bGjStA3F"
oauth_token_secret = "zL1XJpJCWYPGLZV6gotdgqHsea8QT8L6x0l4mFno"

t = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

# print t.get_home_timeline()

try:
    f = open('twits.txt')
    for line in f:
        t.update_status(status=line)
        time.sleep(tempo)
except TwythonError as e:
    print e
