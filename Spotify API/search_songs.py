import auth_manager
name = "yes or no" 
result = auth_manager.sp.search(name)
track_id="https://open.spotify.com/track/2gkVEnpahpE3bQuvGuCpAV" 
track=auth_manager.sp.track(track_id, market=None)
print(track)
import json
with open('data.json', 'w') as f:
    json.dump(track, f)
# result['tracks']['items'][0]['artists']
# print(result)56