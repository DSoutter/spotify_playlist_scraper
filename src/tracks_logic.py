import os.path
from setup_script import sp_oauth as sp 
import csv
current_user_id = sp.current_user()["id"]
csv_header = ["Playlist Name", "Song Name", "Song Popularity", "Artist/Artists", "Album", "Album release date"]

def get_tracks(writer, pl_id):

    pl_tracks = sp.playlist_items(pl_id)["items"]

    for track in pl_tracks:
        # For multiple artists, it needs to loop but only add a comma if there is more than one. 
        artists = ""
        for artist in track["track"]["artists"]:
            if artists:
                artists += ", "
            artists += artist["name"]    

        writer.writerow([sp.playlist(pl_id)["name"],
                         track["track"]["name"],
                         track["track"]["popularity"],
                         artists,
                         track["track"]["album"]["name"],
                         track["track"]["album"]["release_date"]])

def get_ids(writer, pathname):
     with open(pathname, 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)

        for row in csv_reader:
            print('Working on: ' + row[0])
            id = row[2]
            get_tracks(writer, id)

def write_to_csv(pathname):
    data_path = pathname[:-4] + "_data" + pathname[-4:]
    with open(data_path, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a header to the csv file
        writer.writerow(csv_header)
        # Loop for the body of the data
        get_ids(writer, pathname)
