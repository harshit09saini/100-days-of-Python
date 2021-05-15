# Spotify Musical Time Machine Playlist
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

date = input("Enter a date in this format YYYY-MM-DD: ")


scope = "playlist-modify-private playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id="",
                                               client_secret="",
                                               redirect_uri="http://example.com",
                                               show_dialog=True,
                                               cache_path=".cache"
                                               ))

username = sp.current_user()["id"]

# DATE = "2019-12-08"
CLIENT_ID = ""
CLIENT_SECRET = ""
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"

music_response = requests.get(f"{BILLBOARD_URL}/{DATE}")
music_response.raise_for_status()

soup = BeautifulSoup(music_response.content, "html.parser")

song_titles = [titles.getText() for titles in soup.findAll(
    "span", {'class': 'chart-element__information__song'})]
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song}", type="track")
    print(song)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_id = sp.user_playlist_create(
    user=username, name=f"{DATE} PYTHON", public=True)

sp.playlist_add_items(playlist_id=playlist_id["id"], items=song_uris)
