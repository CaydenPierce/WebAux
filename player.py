import vlc, pafy
import sys
from threading import Thread
from getSong import getSongUrl

class Player:
    def __init__(self):
        self.lock = False #this is a little semaphore
        self.playing = False #this is to stop the playing when we want a new song

    def play(self, query):
        songName = getSongUrl(query)
        self.playYoutube(songName)
        
    def playYoutube(self, url):
#        self.playing = False
#        video = pafy.new(url)
#        playurl = video.getbest().url
#
#        Instance = vlc.Instance()
#        player = Instance.media_player_new()
#        Media = Instance.media_new(playurl)
#        Media.get_mrl()
#        player.set_media(Media)
        Thread(target=self.playThread, args=(url,)).start()
        return 1

    def playThread(self, url):
        self.playing = False
        video = pafy.new(url)
        playurl = video.getbest().url

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        while self.lock == True:
            pass
        self.lock = True
        self.playing = True
        player.play()
        good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
        while (str(player.get_state()) in good_states) and (self.playing == True):
            print('Stream is working. Current state = {}'.format(player.get_state()), end="\r")

        print('Stream is done or not working. Current state = {}'.format(player.get_state()))
        player.stop()
        self.playing = False
        self.lock = False
