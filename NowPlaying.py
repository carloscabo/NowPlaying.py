import os
import sys
import json

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

def tweetWithImage( filepath, text ):
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    print('Tw:'+filepath)
    print('Tw:'+text)
    file = open( filepath, 'rb')
    img_data = file.read()
    r = api.request('statuses/update_with_media', {'status': text }, {'media[]':img_data})
    print( 'Twitter status:' + str(r.status_code) )

# json_fn = "/Users/carloscabo/Library/Application Support/Google Play Music Desktop Player/json_store/playback.json"
json_fn = os.environ['HOME'] + "/Library/Application Support/Google Play Music Desktop Player/json_store/playback.json"
tweet_tpl = "#NowPlaying «{{__ALBUM__}}» by {{__ARTIST__}} "

with open( json_fn ) as data_file:
    data = json.load(data_file)
    album = data['song']['album']
    artist = data['song']['artist']
    cover_url = data['song']['albumArt']

    urlretrieve( cover_url, './cover.jpg' )

    tweet = tweet_tpl.replace('{{__ARTIST__}}', artist).replace('{{__ALBUM__}}', album)
    try:
        tweet += sys.argv[1]
    except IndexError:
        print( 'No params' )

    print(tweet)
    tweetWithImage( './cover.jpg', tweet )
