# NowPlaying.py
Python 3 script that tweets #NowPlaying info taken from Google Play Music Desktop Player, including album cover

# Requirements

Obviously you need to have installed the <https://www.googleplaymusicdesktopplayer.com/>, and Python 3.

# usage / config

[Create API Keys for your  yout twitter account](https://dev.twitter.com/oauth/overview/application-owner-access-tokens), add then to a file called `config.yml` in the same place the `NowPlaying.py` script is located. You can use the `config.sample.yml` file as template.

To tweet the curren album with its cover execute in your terminal:

```
python3 NowPlaying.py
```

If you want to add extra comments / tags to the tweet pass them as string parameter:

```
python3 NowPlaying.py 'This is the bes #pop album ever :)'
```
