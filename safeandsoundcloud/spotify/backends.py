import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.util import prompt_for_user_token
from safeandsoundcloud import settings

client_credentials_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CREDENTIAL['CLIENT_ID'],
                                                      client_secret=settings.SPOTIFY_CREDENTIAL['CLIENT_SECRET'])

token=None
try:
    token = prompt_for_user_token(
        username="frstylskier46",
        client_id=settings.SPOTIFY_CREDENTIAL['CLIENT_ID'],
        client_secret=settings.SPOTIFY_CREDENTIAL['CLIENT_SECRET'],
        redirect_uri='http://localhost:8080/spotify/callback/')
except:
    pass

sp = spotipy.Spotify(auth=token)

sp = spotipy.Spotify()
playlists = sp.user_playlists('frstylskier46')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None