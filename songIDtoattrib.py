import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:track:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
results2 = spotify.audio_features([birdy_uri])
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
