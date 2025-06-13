import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

week_date = input("Enter in date (YYYY-MM-DD): ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

URL = f"https://www.billboard.com/charts/hot-100/{week_date}"

# Write your code below this line 
response = requests.get(url=URL, headers=header)
response.encoding = "utf-8"
bb100_webpage = response.text

soup = BeautifulSoup(bb100_webpage, "html.parser")
print(soup.title.getText())
#print(soup.prettify())

song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]
idx = 1
for song in song_names:
    print(f"{idx}. {song}")
    idx += 1

myclientid = os.getenv("XXX")
mysecret = os.getenv("XXX")
myurl = os.getenv("XXX")

scope = scope = "user-library-read playlist-modify-private playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="XXX", client_secret="XXXX2", redirect_uri="https://example.com",  scope=scope))

spotify_username = sp.current_user()["display_name"]

print(f"\nSpotify User Name: {spotify_username}\n")

song_uris = []
for song in song_names:
    try:
        result = sp.search(q=f"track:{song}", type="track", limit=1)
        #pprint.pp(result)
        if result["tracks"]["items"]:
            song_uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error finding {song}: {e}")

playlist_title =f"{week_date} Billboard 100"
playlist_id = sp.user_playlist_create(spotify_username, playlist_title, public=True, collaborative=False, description="Top 100 Hits from Your Birthday")["id"]
print(f"Playlist Name: {playlist_title} Playlist ID: {playlist_id}")

print(f"Spotify Song URIs: {len( song_uris)}")
for song_uri in song_uris:
    if playlist_id:
        sp.playlist_add_items(playlist_id, [song_uri], position=None )
        
    print(song_uri)
    


