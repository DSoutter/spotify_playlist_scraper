import os.path
from setup_script import sp_oauth as sp 

current_user_id = sp.current_user()["id"]

def get_playlists(offset):
    user_playlists = sp.current_user_playlists(50, offset)["items"]

    for item in user_playlists:
        if item["owner"]["id"] == current_user_id:
            print("Playlist Name: " + item["name"])
            print("Tracks: " + str(item["tracks"]["total"]))
   