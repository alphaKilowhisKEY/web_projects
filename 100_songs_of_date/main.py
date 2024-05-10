'''
Billboard Hot 100 Playlist Creator

This Python script allows you to create a Spotify playlist based on Billboard Hot 100 songs for a specific date.

Requirements:
- Python 3.x
- `spotipy` library
- `beautifulsoup4` library
- Spotify Developer Account (for obtaining client ID and client secret)

Note:
+ Obtain Spotify API credentials (client ID and client secret) by creating a Spotify Developer Account: https://developer.spotify.com/dashboard/
+ Replace `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` variables in the script with your obtained credentials.

Usage:
1. > python3 main.py
2. Enter a date in the format `YYYY-MM-DD` when prompted.
3. The script will scrape Billboard Hot 100 songs for the entered date, search for them on Spotify, and create a private playlist with the found songs.

'''

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
import os

SPOTIFY_CLIENT_ID = "********"
SPOTIFY_CLIENT_SECRET = "********"

user_input_date = input("Give a date in this format YYYY-MM-DD: ")
song_names = []

# Scraping
response = requests.get("https://www.billboard.com/charts/hot-100/" + user_input_date)

if response == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    span_song_names = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in span_song_names]
else:
    print("Status Code was not 200.")

# Authentication in Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = user_input_date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{user_input_date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)