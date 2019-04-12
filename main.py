#!/raspi/bin/python
import threading
import time
from list import List

import vlc
from youtube import Youtube


def play_vlc(audio_url, queue):
    instance = vlc.Instance("--novideo -q")
    player = instance.media_player_new()
    media = instance.media_new(audio_url.url)
    player.set_media(media)
    player.play()
    x = 0
    while player.get_length() < 1:
        time.sleep(0.05)
    time.sleep(player.get_length() / 1000)
    queue.remove()


def main():
    t = None
    queue = List()
    ytb = Youtube()
    url = ytb.get_one('thunderstruck')
    pafy = ytb.get_audio(url)
    queue.add(pafy)
    t = threading.Thread(target=play_vlc, args=(queue.queue[0], queue))
    t.start()


if __name__ == '__main__':
    main()
