import os.path
import spotipy
from spotipy.oauth2 import SpotifyOAuth 
import csv

# Check if there's a spotify_credentials.py file
# Ask user if they have a path and paste if so
file_exists = input("Do you have a spotify_credentials.py file? (Y/N): ")
if file_exists == "Y":
    file_path = input("Please enter your file path to this file: ")
    client_id = 'from file to be added'
    print("Client_ID is: " + client_id)

    client_secret = 'from file to be added'
    print("Client_Secret is: " + client_secret)
else:
    client_id = input("Enter Client_ID: ")
    print("Client_ID is: " + client_id)

    client_secret = input("Enter Client_Secret: ")
    print("Client_Secret is: " + client_secret)
  
#if os.path.isfile(/Users/duncan/Documents/Programming/spotify_playlist_scraper/src)

redirect_uri = 'https://localhost:3000'
print (redirect_uri)