import spotipy
from spotipy.oauth2 import SpotifyOAuth  

CLIENT_ID = input("Enter Client_ID: ")
CLIENT_SECRET = input("Enter Client_Secret: ")
REDIRECT_URI = input("Enter Redirect URI: ")
PATH = input("Enter the folder location you want to use, such as '/Users/duncan/Downloads': ").rstrip('/') + '/playlists.csv'
scope = "playlist-read-private"
auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)
sp_oauth = spotipy.Spotify(auth_manager=auth_manager)