import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
client_id = "[Add you client id]"
client_secret = "[Add your client secret]"
redirect_uri = "[Add your uri]"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
