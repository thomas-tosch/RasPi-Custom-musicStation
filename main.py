from threading import Thread
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
    while player.get_length() < 1:
        time.sleep(0.05)
    time.sleep(player.get_length() / 1000)
    queue.remove()


def add_song(name, list):
    startTime = time.time()
    ytb = Youtube()
    print("ytb " + str(time.time() - startTime))
    url = ytb.get_one(name)
    print("url " + str(time.time() - startTime))
    pafy = ytb.get_audio(url)
    print("pafy " + str(time.time() - startTime))
    list.add(pafy)
    print("list " + str(time.time() - startTime))


def play_after_this_one(name, list):
    ytb = Youtube()
    url = ytb.get_one(name)
    pafy = ytb.get_audio(url)
    list.add(pafy)


def main():
    t = None
    list = List()
    Thread(target=add_song, args=('thunderstruck', list)).start()
    Thread(target=add_song, args=('redbone', list)).start()
    while True:
        if list.queue is None or not list.queue:
            time.sleep(0.2)
        elif t is None:
            t = Thread(target=play_vlc, args=(list.queue[0], list))
            t.start()
        elif not t.is_alive():
            t = Thread(target=play_vlc, args=(list.queue[0], list))
            t.start()

if __name__ == '__main__':
    main()
