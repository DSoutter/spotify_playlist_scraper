# Spotify API Scraper to download an offline list of users playlists
## Used to have a backup of all your playlists in case for whatever reason, you cannot access your playlists and want to keep them somewhere safe

Two csv's will be created, the first is a summary of all playlists with the following headers:
1. Playlist Name
2. Number of songs

The second will have a summary of all the songs in the playlists:
1. Playlist Name
2. Song Name
3. Artist/Artists
4. Album
5. Album release date
6. Popularity


# How to run:
1. Fork the code and pull it onto your computer
2. Go to: https://developer.spotify.com/dashboard/create
3. Create an app with whatever name and description you like, the Redirect URI can also be anything but I suggest https://localhost:3000
4. Tick Web API and create
5. Once created, go to Settings and click View client secret
6. Open a terminal window and cd to the project folder. 
7. Run the script as so: python3 src/running_script.py
8. Follow the instructions by pasting in the three different values and then the filepath.
9. Then insert the URL that you were redirected to.
10. That's it, you should now have the two files downloaded in the folder location you chose.
11. If you want to run again on a different username, make sure to delete the .cache file created