import os.path
import spotipy
from spotipy.oauth2 import SpotifyOAuth 
import csv

# Check if there's a spotify_credentials.py file
# Ask user if they have a path and paste if so
file_exists = input("Do you have a spotify_credentials.py file? (Y/N): ")
if file_exists.upper() == "Y":
    try:
        import spotify_credenntials as creds
        client_id = creds.CLIENT_ID
        print("Client_ID is: " + client_id)

        client_secret = creds.CLIENT_SECRET
        print("Client_Secret is: " + client_secret)
    except:
        print('Check the file is called "spotify_credentials.py" and is stored in the src folder.')
        print('There should be two variables "CLIENT_ID" and "CLIENT_SECRET"')


else:
    client_id = input("Enter Client_ID: ")
    print("Client_ID is: " + client_id)

    client_secret = input("Enter Client_Secret: ")
    print("Client_Secret is: " + client_secret)
  
redirect_uri = 'https://localhost:3000'
print (redirect_uri)
