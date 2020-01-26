import vlc, pafy
import sys

def playYoutube(url):
    video = pafy.new(url)
    playurl = video.getbest().url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
    while str(player.get_state()) in good_states:
        print('Stream is working. Current state = {}'.format(player.get_state()), end="\r")

    print('Stream is done or not working. Current state = {}'.format(player.get_state()))
    player.stop()
