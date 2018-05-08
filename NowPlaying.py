# -*- coding: utf-8 -*-

"""NowPlaying.py: script that tweets #NowPlaying info taken from Google Play Music Desktop Player, including album cover."""
__author__  = "Carlos Cabo"
__license__ = "MIT"
__version__ = "1.0.3"

import os
import sys
import json
import platform
import argparse

import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve

from TwitterAPI import TwitterAPI

import yaml
config = yaml.load(open('./config.yml'))
CONSUMER_KEY        = config['TwitterAPI']['CONSUMER_KEY']
CONSUMER_SECRET     = config['TwitterAPI']['CONSUMER_SECRET']
ACCESS_TOKEN_KEY    = config['TwitterAPI']['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = config['TwitterAPI']['ACCESS_TOKEN_SECRET']

json_fn = ''
if platform.system() == 'Windows':
    json_fn = os.getenv('APPDATA') + "\Google Play Music Desktop Player\json_store\playback.json"
else: # MacOS
    json_fn = os.environ['HOME'] + "/Library/Application Support/Google Play Music Desktop Player/json_store/playback.json"
print(json_fn)

def tweetWithImage( filepath, text ):
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    print('Tw:'+filepath)
    print('Tw:'+text)
    file = open( filepath, 'rb')
    img_data = file.read()
    r = api.request('statuses/update_with_media', {'status': text }, {'media[]':img_data})
    print( 'Twitter status:' + str(r.status_code) )

# json_fn = "/Users/carloscabo/Library/Application Support/Google Play Music Desktop Player/json_store/playback.json"
tweet_tpl = "#NowPlaying «{{__ALBUM__}}» by {{__ARTIST__}} "

with open( json_fn, encoding='utf-8' ) as data_file:

    data = json.load(data_file)
    album = data['song']['album']
    artist = data['song']['artist']
    cover_url = data['song']['albumArt']
    print( data )
    print( "\n" )

    if 'default_album_med.png' in cover_url:
        print('HAS NO COVER!!!')
        sys.exit()

    urlretrieve( cover_url, './cover.jpg' )

    if len(sys.argv) == 2:
        if sys.argv[1].lower() == '--v' or sys.argv[1].lower() == '--va':
            artist = 'Various Artists'
        else:
            tweet_tpl += sys.argv[1]

    if len(sys.argv) == 3:
        tweet_tpl += sys.argv[2]

    tweet = tweet_tpl.replace('{{__ARTIST__}}', artist).replace('{{__ALBUM__}}', album)
    print(tweet)
    tweetWithImage( './cover.jpg', tweet )
