import os.path
import spotipy
from spotipy.oauth2 import SpotifyOAuth  

# Check if there's a spotify_credentials.py file
file_exists = input("Do you have a spotify_credentials.py file? (Y/N): ")
while file_exists.upper() not in ("Y", "N"):
    file_exists = input("You did not enter \"Y\" or \"N\", try again: ")

if file_exists.upper() == "Y":
    try:
        import spotify_credentials as creds
        SPOTIPY_CLIENT_ID = creds.CLIENT_ID
        SPOTIPY_CLIENT_SECRET = creds.CLIENT_SECRET
    except:
        print("Check the file is called \"spotify_credentials.py\" and is stored in the src folder.")
        print("There should be two variables \"CLIENT_ID\" and \"CLIENT_SECRET\"")

elif file_exists.upper() == "N":
    SPOTIPY_CLIENT_ID = input("Enter Client_ID: ")
    SPOTIPY_CLIENT_SECRET = input("Enter Client_Secret: ")

SPOTIPY_REDIRECT_URI = "https://localhost:3000"

scope = "playlist-read-private"
auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope)
sp_oauth = spotipy.Spotify(auth_manager=auth_manager) 
