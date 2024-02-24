import spotipy
from spotipy.oauth2 import SpotifyOAuth
import auth_manager
SPOTIPY_CLIENT_ID = "82161998342f4d75adf9faea56dee308"
SPOTIPY_CLIENT_SECRET = "a56dd02efa5c4c9eb05645d0f708650d"
scope = auth_manager.credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri="http://example.com"))
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])