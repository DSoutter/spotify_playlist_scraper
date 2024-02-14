import os.path
from setup_script import sp_oauth as sp 
import csv
current_user_id = sp.current_user()["id"]
csv_header = ["Playlist Name", "Number of Songs", "Playlist Id"]

def get_playlists(writer):
    offset = 0
    while True:
        user_playlists = sp.current_user_playlists(50, offset)["items"]
        if user_playlists ==[]:
            break
        for item in user_playlists:
            if item == []:
                break
            if item["owner"]["id"] == current_user_id:
                writer.writerow([item["name"], str(item["tracks"]["total"]), item["uri"][17:39]])
        offset += 50
def write_to_csv(pathname):
    with open(pathname, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a header to the csv file
        writer.writerow(csv_header)
        # Loop for the body of the data
        get_playlists(writer)
