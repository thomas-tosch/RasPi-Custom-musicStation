#!/raspi/bin/python
import time
import vlc
from youtube import Youtube as ytb


def play_vlc(audio_url):
    instance = vlc.Instance("--novideo -q")
    player = instance.media_player_new()
    media = instance.media_new(audio_url.url)
    player.set_media(media)
    player.play()
    x = 0
    while player.get_length() < 1:
        time.sleep(0.05)
    time.sleep(player.get_length() / 1000)


def main():
    url = ytb.get_one('thunderstruck')
    pafy = ytb.get_audio(url)
    ytb.
    play_vlc(pafy)


if __name__ == '__main__':
    main()
