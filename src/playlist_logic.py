import os.path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
user = sp.user('dsoutter')
playlists = sp.user_playlists('dsoutter')
get_playlists = print(user["display_name"])
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None