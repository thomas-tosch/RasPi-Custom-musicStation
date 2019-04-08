#!/raspi/bin/python
import time

import requests
import pafy
import vlc

token = "AIzaSyC5s6T1G9EC6Z3ZXldv0-2OyxEny3gMr8k"
endpoint = 'https://www.googleapis.com/youtube/v3/'


def get_one_url(query):
    result = requests.get(endpoint+'search', params={
        'part': 'id, snippet',
        'fields': 'items/id/videoId',
        'maxResults': 1,
        'type': 'video',
        'q': query,
        'key': token
    })
    return "https://www.youtube.com/watch?v=" + str(result.json()['items'][0]['id']['videoId'])


def get_audio(url):
    video = pafy.new(url)
    return video.getbestaudio("m4a")


def play_vlc(audio_url):
    instance = vlc.Instance("--novideo -q")
    player = instance.media_player_new()
    media = instance.media_new(audio_url.url)
    player.set_media(media)
    player.play()
    # Can become very complicated (check when audio pops)
    time.sleep(1)
    time.sleep(player.get_length() / 1000)


def main():
    url = get_one_url('bruh v2')
    pafy = get_audio(url)
    play_vlc(pafy)


if __name__ == '__main__':
    main()
