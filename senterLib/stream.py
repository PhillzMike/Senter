# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:47:49 2018

@author: Jedidiah & Timilehin
"""
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# consumer key, consumer secret, access token, access secret.
ckey = "cWdTq9cHpSJIx0CC6wmBT80oi"
csecret = "	fYFfPEN8sU1NPxnUHMYZotbRL12q5lkGpvtYeoDDVqdvMhexdg"
atoken = "723833280-raF2otES87QBynHxC3EKJxQR5j2zsgGhXjhsRjHp"
asecret = "bkm3xCnQJHo5wURxSc4hpP0qyWsIO6UVIbjA2Y0Niy8PA"


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        # username = all_data["user"]["screen_name"]

        print((tweet))

        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])


