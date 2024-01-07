import os.path
from setup_script import sp_oauth as sp 
import csv
current_user_id = sp.current_user()["id"]
csv_header = ["Playlist Name", "Song Name", "Song Popularity", "Artist/Artists", "Album", "Album release date"]
playlist_id = "6xjb4RLYCxd1rEQD5g6LGv"

def get_tracks(writer, offset):
    pl_tracks = sp.playlist_items(playlist_id)["items"]

    for track in pl_tracks:
        # For multiple artists, it needs to loop but only add a comma if there is more than one. 
        artists = ""
        for artist in track["track"]["artists"]:
            if artists:
                artists += ", "
            artists += artist["name"]    

        writer.writerow([sp.playlist(playlist_id)["name"],
                         track["track"]["name"],
                         track["track"]["popularity"],
                         artists,
                         track["track"]["album"]["name"],
                         track["track"]["album"]["release_date"]])

def write_to_csv():
    with open('/Users/duncan/Downloads/playlist_data.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a header to the csv file
        writer.writerow(csv_header)
        # Loop for the body of the data
        get_tracks(writer, 0)
