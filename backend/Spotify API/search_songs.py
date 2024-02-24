import auth_manager
name = "yes or no" 
result = auth_manager.sp.search(name)
track_id="https://open.spotify.com/track/2gkVEnpahpE3bQuvGuCpAV" 
track=auth_manager.sp.track(track_id, market=None)
#print(track)
image_url = track['album']['images'][2]['url']
artist_name = track['artists'][0]['name']
track_url = track['external_urls']['spotify']
track_id = track['id']
track_uri = track['uri']
song_data=[image_url,artist_name,track_url,track_id,track_uri]
print(song_data)
