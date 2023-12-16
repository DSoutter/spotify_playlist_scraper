import os.path
from setup_script import sp_oauth as sp 
import csv
current_user_id = sp.current_user()["id"]
csv_header = ["Playlist Name", "Song Name", "Artist/Artists", "Album", "Album release date", "Song Popularity"]
playlist_id = '4dOQIqHSfcmFXtPm79lMNn'

def get_songs(writer, offset):
    user_playlists = sp.current_user_playlists(50, offset)["items"]

    for item in user_playlists:
        if item["owner"]["id"] == current_user_id:
            writer.writerow([item["name"], str(item["tracks"]["total"]), item["uri"][17:39]])
            print(item)

def write_to_csv():
    with open('/Users/duncan/Downloads/playlist_songs.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a header to the csv file
        writer.writerow(csv_header)
        # Loop for the body of the data
        get_playlists(writer, 0)
