# RasPi-Custom-musicStation
- http server with no front end (for now)
- takes post request to play, stop, resume, pause, add song to queue..
- sends to mosyt or similar end-product inscructions
- manages a queue that can add or remove
- allows skips
- takes input from google assistant hotwords
- Go ? Deoends on the end-product libraries. (mps is py)

v1.1

- uses youtube api to query search
- uses youtubemp3api to get mp3 file stream
- shouls have a front-end with a search box that returns the list of results
- hotword plays "im feeling lucky" result

v1.2

- pafy apparently does query to mp3 directly from youtibe too
- vlc can stream from both mp3 solutions and includes player functions
- maybe vlc has a queue ?
