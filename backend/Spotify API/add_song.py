import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import auth_manager
client_id = auth_manager.client_id
client_secret = auth_manager.client_secret
redirect_uri = auth_manager.redirect_uri
scope = "user-read-playback-state,user-modify-playback-state"

sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
          client_id=client_id,
          client_secret=client_secret,
          redirect_uri=redirect_uri,    
          scope=scope, open_browser=False,))

# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
sp.add_to_queue('spotify:track:1HfMVBKM75vxSfsQ5VefZ5',device_id=None)
