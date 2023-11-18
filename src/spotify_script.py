import os.path
import playlist_logic as pl

# Check if there's a spotify_credentials.py file
# Ask user if they have a path and paste if so
file_exists = input("Do you have a spotify_credentials.py file? (Y/N): ")
if file_exists.upper() == "Y":
    try:
        import spotify_credentials as creds
        SPOTIPY_CLIENT_ID = creds.CLIENT_ID
        print("Client_ID is: " + SPOTIPY_CLIENT_ID)

        SPOTIPY_CLIENT_SECRET = creds.CLIENT_SECRET
        print("Client_Secret is: " + SPOTIPY_CLIENT_SECRET)
    except:
        print('Check the file is called "spotify_credentials.py" and is stored in the src folder.')
        print('There should be two variables "CLIENT_ID" and "CLIENT_SECRET"')


else:
    SPOTIPY_CLIENT_ID = input("Enter Client_ID: ")
    print("Client_ID is: " + SPOTIPY_CLIENT_ID)

    SPOTIPY_CLIENT_SECRET = input("Enter Client_Secret: ")
    print("Client_Secret is: " + SPOTIPY_CLIENT_SECRET)
  
SPOTIPY_REDIRECT_URI = 'https://localhost:3000'
print (SPOTIPY_REDIRECT_URI)

pl.get_playlists()