import os.path
from setup_script import sp_oauth as sp 
import csv
current_user_id = sp.current_user()["id"]
csv_header = ["Playlist Name", "Song Name", "Song Popularity", "Artist/Artists", "Album", "Album release date"]
playlist_id = "4dOQIqHSfcmFXtPm79lMNn"

def get_tracks(writer, offset):
    playlist_tracks = sp.current_user_playlists(50, offset)["items"]

    for item in user_playlists:
        if item["owner"]["id"] == current_user_id:
            writer.writerow([item["name"], str(item["tracks"]["total"]), item["uri"][17:39]])
            print(item)

def write_to_csv():
    print("Playlist Name:")
    print(sp.playlist(playlist_id)["name"])
    print("Song Name:")
    print(sp.playlist_items(playlist_id)["items"][0]["track"]["name"])
    print("Song Popularity:")
    print(sp.playlist_items(playlist_id)["items"][0]["track"]["popularity"])
    print("Artist/Artists:")
    for artist in sp.playlist_items(playlist_id)["items"][0]["track"]["artists"]:
        if artist != sp.playlist_items(playlist_id)["items"][0]["track"]["artists"][0]:
            print(", ")
        print (artist["name"])
    print("Album:")
    print(sp.playlist_items(playlist_id)["items"][0]["track"]["album"]["name"])
    print("Album release date:")
    print(sp.playlist_items(playlist_id)["items"][0]["track"]["album"]["release_date"])
    # with open('/Users/duncan/Downloads/playlist_songs.csv', 'w') as f:
    #     # create the csv writer
    #     writer = csv.writer(f)
    #     # write a header to the csv file
    #     writer.writerow(csv_header)
    #     # Loop for the body of the data
    #     get_playlists(writer, 0)
