import requests
import pafy


class Youtube:

    @property
    def token(self):
        return "AIzaSyC5s6T1G9EC6Z3ZXldv0-2OyxEny3gMr8k"

    @property
    def endpoint(self):
        return "https://www.googleapis.com/youtube/v3/"

    def get_one(self, query):
        result = requests.get(self.endpoint + 'search', params={
            'part': 'id, snippet',
            'fields': 'items/id/videoId',
            'maxResults': 1,
            'type': 'video',
            'q': query,
            'key': self.token
        })
        return "https://www.youtube.com/watch?v=" + str(result.json()['items'][0]['id']['videoId'])

    def get_ten(self, query):
        result = requests.get(self.endpoint + 'search', params={
            'part': 'id, snippet',
            'fields': 'items/id/videoId',
            'maxResults': 10,
            'type': 'video',
            'q': query,
            'key': self.token
        })
        return "https://www.youtube.com/watch?v=" + str(result.json()['items'][0]['id']['videoId'])

    @staticmethod
    def get_audio(url):
        return pafy.new(url).getbestaudio("m4a")
