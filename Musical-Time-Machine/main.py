import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv(".env.txt")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

while True:
    travel_to_date = input("What year would you like to travel to (YYYY-MM-DD)?")
    # travel_to_date = "1998-08-13"
    year = travel_to_date.split("-")[0]
    url = f"https://www.billboard.com/charts/hot-100/{travel_to_date}/"

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

    try:
        response = requests.get(url=url, headers=header)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("That didn't work. Please ensure correct date format.")
    else:
        break

billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, features="html.parser")

songs = [song.getText().strip() for song in soup.select("li ul li h3")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

songs_uris = []

for track in songs:
    response = sp.search(q=f"track: {track}: {year}", type="track", limit=1)
    try:
        uri = response["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{track} can't be found in Spotify")

# print(songs_uris)
playlist_name = f"Billboard Hot 100 for {travel_to_date}"
playlist_description = f"Playlist featuring the Billboard Hot 100 tracks for the week of {travel_to_date}"
playlist = sp.user_playlist_create(user= user_id,
                                   name= playlist_name,
                                   public=False,
                                   collaborative=False,
                                   description= playlist_description)

playlist_id = playlist["id"]
playlist_add = sp.playlist_add_items(playlist_id = playlist_id, items= songs_uris, position= None)



