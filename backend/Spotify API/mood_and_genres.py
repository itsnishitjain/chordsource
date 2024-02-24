import auth_manager_copy

def get_artist_genres(artist_id):
  artist = auth_manager_copy.sp.artist(artist_id)
  return artist['genres']


def detect_song_genre(track_id):
  track = auth_manager_copy.sp.track(track_id)
  artists = track['artists']

  all_genres = []
  for artist in artists:
    artist_genres = get_artist_genres(artist['id'])
    all_genres.extend(artist_genres)

  return all_genres


def find_track_genres(track_ids):
  genre_counts = {}
  total_tracks = len(track_ids)

  for track_id in track_ids:
    track_genres = detect_song_genre(track_id)[0]  #song's first main genre
    genre_counts[track_genres] = genre_counts.get(track_genres, 0) + 1

  # Calculate percentages
  genre_percentages = {
      genre: (count / total_tracks) * 100
      for genre, count in genre_counts.items()
  }
  return genre_percentages


# Example usage
track_ids = [
    'https://open.spotify.com/track/2gkVEnpahpE3bQuvGuCpAV',
    'https://open.spotify.com/track/561jH07mF1jHuk7KlaeF0s',
    'https://open.spotify.com/track/0maCwhZTO3PybhSiQcsjAf',
    'https://open.spotify.com/track/4UkUxO2WlKLc0Q1iEutGGh',
    'https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR'
]
genre_percentages = find_track_genres(track_ids)
print("Genres and their percentages:")
for genre, percentage in genre_percentages.items():
  print(f"{genre}: {percentage:.2f}%")
  
#=========================WHEN HISTORY IS MADE!!!============
def detect_mood(valence, energy):
    if valence > 0.5 and energy > 0.5:
        return "Happy and Energetic"
    elif valence <= 0.5 and energy > 0.5:
        return "Sad but Energetic"
    elif valence > 0.5 and energy <= 0.5:
        return "Happy but Calm"
    else:
        return "Sad and Calm"

# Initialize counters for mood classification
happy_count = 0
sad_count = 0
energetic_count = 0
calm_count = 0

# Iterate over track IDs
for track_id in track_ids:
    # Get audio features
    audio_features = auth_manager_copy.sp.audio_features(track_id)[0]
    # print("Audio Features:", audio_features)

    # Extract relevant audio features
    valence = audio_features['valence']
    energy = audio_features['energy']

    # Detect mood
    mood = detect_mood(valence, energy)
    
    # Update counters based on detected mood
    if "Happy" in mood:
        happy_count += 1
    elif "Sad" in mood:
        sad_count += 1
    if "Energetic" in mood:
        energetic_count += 1
    elif "Calm" in mood:
        calm_count += 1

# Determine overall mood based on dominant characteristics
overall_mood = ""
if happy_count > sad_count:
    overall_mood += "Happy "
elif sad_count > happy_count:
    overall_mood += "Sad "
if energetic_count > calm_count:
    overall_mood += "and Energetic"
elif calm_count > energetic_count:
    overall_mood += "and Calm"

print("Overall Mood:", overall_mood)
