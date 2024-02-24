import base64
import webbrowser
import urllib.parse

import requests
client_id = ""
client_secret = ""
code=""
auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "user-library-read"
}

#webbrowser.open("https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(auth_headers))
credentials={
"SPOTIPY_CLIENT_ID":"",
"SPOTIPY_CLIENT_SECRET":""
}

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
token = r.json()["access_token"]
token =""
print(token)


user_headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

user_params = {
    "limit": 50,
}
track_id = "2gkVEnpahpE3bQuvGuCpAV"
user_tracks_response = requests.get(f"https://api.spotify.com/v1/me/tracks/{track_id}", params=user_params, headers=user_headers)

print(user_tracks_response.json())

