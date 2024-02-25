from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from spotipy import SpotifyOAuth, Spotify
from datetime import datetime
import waitress
import threading
import logging
import random
import time
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'todo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
db = SQLAlchemy(app)

load_dotenv()
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
    redirect_uri='http://localhost:7777/callback',
    scope='user-read-playback-state,user-modify-playback-state'
))


class Queue(db.Model):
    song_url = db.Column(db.String(128), nullable=False, primary_key=True)
    score = db.Column(db.Float, nullable=False)
    rawscore = db.Column(db.Float, nullable=False)
    multiplier = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.BigInteger, nullable=False)


class History(db.Model):
    song_url = db.Column(db.String(128), nullable=False, primary_key=True)
    timestamp = db.Column(db.BigInteger, nullable=False)


class Genres(db.Model):
    genre = db.Column(db.Text, nullable=False, primary_key=True)
    count = db.Column(db.BigInteger, nullable=False)


class Features(db.Model):
    feature = db.Column(db.Text, nullable=False, primary_key=True)
    value = db.Column(db.Float, nullable=False)


class SpotifySong(db.Model):
    url = db.Column(db.String(128), nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    duration_ms = db.Column(db.BigInteger, nullable=False)
    image_url = db.Column(db.String(128), nullable=False)
    album = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    genres = db.Column(db.Text, nullable=False)
    acousticness = db.Column(db.Float, nullable=False)
    danceability = db.Column(db.Float, nullable=False)
    energy = db.Column(db.Float, nullable=False)
    liveness = db.Column(db.Float, nullable=False)
    tempo = db.Column(db.Float, nullable=False)
    valence = db.Column(db.Float, nullable=False)

    def get(url):
        song = SpotifySong.query.filter_by(url=url).first()
        if song is None:
            app.logger.info(f'Fetching song info for {url}...')
            track = sp.track(url, market=None)
            album = sp.album(track['album']['uri'])
            artist = sp.artist(track['artists'][0]['uri'])
            features = sp.audio_features(url)
            song = SpotifySong(
                url=url,
                name=track['name'],
                duration_ms=track['duration_ms'],
                image_url=album['images'][2]['url'],
                album=album['name'],
                artist=artist['name'],
                genres='\t'.join(album['genres'] + artist['genres']),
                acousticness=features[0]['acousticness'],
                danceability=features[0]['danceability'],
                energy=features[0]['energy'],
                liveness=features[0]['liveness'],
                tempo=features[0]['tempo'],
                valence=features[0]['valence'])
            db.session.add(song)
            db.session.commit()
        return song

    def get_info(url):
        song = SpotifySong.get(url)
        return {
            'url': song.url,
            'name': song.name,
            'duration_ms': song.duration_ms,
            'image_url': song.image_url,
            'album': song.album,
            'artist': song.artist,
            'genres': song.genres.split('\t'),
            'features': {
                'acousticness': song.acousticness,
                'danceability': song.danceability,
                'energy': song.energy,
                'liveness': song.liveness,
                'tempo': song.tempo,
                'valence': song.valence,
            }
        }


@app.route('/status', methods=['GET'])
@cross_origin()
def get_status():
    app.logger.info('/status request')

    queue = [
        {
            'song': SpotifySong.get_info(entry.song_url),
            'score': entry.score,
            'rawscore': entry.rawscore,
            'multiplier': entry.multiplier,
            'timestamp': entry.timestamp,
        } for entry in Queue.query.all()
    ]

    history = [
        {
            'song': SpotifySong.get_info(entry.song_url),
            'timestamp': entry.timestamp,
        } for entry in History.query.all()
    ]

    queue.sort(key=lambda x: x['score'])
    history.sort(key=lambda x: x['timestamp'])

    return {
        'genres': {entry.genre: entry.count for entry in Genres.query.all()},
        'features': {entry.feature: entry.value for entry in Features.query.all()},
        'queue': queue,
        'history': history,
    }


@app.route('/vote', methods=['POST'])
@cross_origin()
def post_vote():
    app.logger.info('/vote request')

    song_url = "https://open.spotify.com/track/" + request.args.get('url')
    if song_url is None or song_url == '':
        app.logger.warning('Missing song URL')
        return {'err': 'Missing song URL'}, 400

    now = datetime.utcnow().timestamp()
    entry = Queue.query.filter_by(song_url=song_url).first()

    if entry is None:
        # Fetch song info from local cache or Spotify API
        song = SpotifySong.get(song_url)
        # Determine multiplier for new song
        multiplier = 1
        for genre in song.genres.split('\t'):
            entry = Genres.query.filter_by(genre=genre).first()
            if entry is not None:
                multiplier += entry.count
        # Insert the new song into queue
        db.session.add(Queue(song_url=song_url, score=multiplier, rawscore=1, multiplier=multiplier, timestamp=now))
        app.logger.info(f'Accepted vote for new entry {song_url}')
    else:
        # Reject duplicate votes
        try:
            if entry.timestamp <= float(session[song_url]):
                app.logger.info(f'Rejected duplicate vote for {song_url}')
                return {'err': 'Already voted for this song URL'}, 403
        except (KeyError, ValueError):
            pass
        # Increase score by one vote
        entry.rawscore += 1
        entry.score += entry.multiplier
        app.logger.info(f'Accepted vote for {song_url}')

    db.session.commit()
    session.permanent = True
    session[song_url] = now
    return {}


with app.app_context():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[logging.FileHandler('instance/output.log'), logging.StreamHandler()])

    db.create_all()
    threading.Thread(target=lambda: waitress.serve(app, host='0.0.0.0', port=8080)).start()

    app.logger.info(f'Authenticated as {sp.current_user()["display_name"]}')
    sp.shuffle(False)
    sp.repeat('off')
    while True:
        try:
            now = datetime.utcnow().timestamp()

            # Play next top queue song
            player = sp.currently_playing()
            if player is not None and player['is_playing']:
                delay = (player['item']['duration_ms'] - player['progress_ms']) / 1000
            elif len(Queue.query.all()) != 0:
                entry = Queue.query.order_by(Queue.score.desc()).first()
                song = SpotifySong.get(entry.song_url)
                sp.start_playback(uris=[entry.song_url])
                hist_entry = History.query.filter_by(song_url=entry.song_url).first()
                if hist_entry is None:
                    db.session.add(History(song_url=entry.song_url, timestamp=now))
                else:
                    hist_entry.timestamp = now
                db.session.delete(entry)
                db.session.commit()
                delay = song.duration_ms / 1000
            else:
                delay = 1

            # Remove any old stragglers from queue
            for entry in Queue.query.filter(Queue.score < 0).all():
                db.session.delete(entry)
            db.session.commit()

            # Figure out current vibe from recent history of features and genres
            genres = {}
            total_acousticness = 0
            total_danceability = 0
            total_energy = 0
            total_liveness = 0
            total_tempo = 0
            total_valence = 0
            count = 0
            for entry in History.query.filter(History.timestamp > now - 1800).all():
                song = SpotifySong.get(entry.song_url)
                for genre in song.genres.split('\t'):
                    genres[genre] = genres[genre] + 1 if genre in genres else 1
                total_acousticness += song.acousticness
                total_danceability += song.danceability
                total_energy += song.energy
                total_liveness += song.liveness
                total_tempo += song.tempo
                total_valence += song.valence
                count += 1
            Genres.query.delete()
            for genre, count in genres.items():
                db.session.add(Genres(genre=genre, count=count))
            Features.query.delete()
            average_acousticness = total_acousticness/count if count else 0
            average_danceability = total_danceability/count if count else 0
            average_energy = total_energy/count if count else 0
            average_liveness = total_liveness/count if count else 0
            average_tempo = total_tempo/count if count else 0
            average_valence = total_valence/count if count else 0
            db.session.add(Features(feature='acousticness', value=average_acousticness))
            db.session.add(Features(feature='danceability', value=average_danceability))
            db.session.add(Features(feature='energy', value=average_energy))
            db.session.add(Features(feature='liveness', value=average_liveness))
            db.session.add(Features(feature='tempo', value=average_tempo))
            db.session.add(Features(feature='valence', value=average_valence))
            db.session.commit()

            # Ensure enough songs are in queue
            if len(Queue.query.all()) < 3:
                app.logger.info('Generating suggestions for the queue...')
                bad_song_urls = [entry.song_url for entry in Queue.query.all() + History.query.filter(History.timestamp > now - 1800).all()]
                seed_tracks = [entry.song_url for entry in History.query.order_by(History.timestamp.desc()).limit(5).all()]
                if len(seed_tracks) == 0:
                    seed_tracks.append('https://open.spotify.com/track/2gkVEnpahpE3bQuvGuCpAV')
                # song_urls = [track['external_urls']['spotify'] for track in sp.recommendations(seed_tracks=seed_tracks)['tracks']]
                song_urls = [
                    'https://open.spotify.com/track/2gkVEnpahpE3bQuvGuCpAV',
                    'https://open.spotify.com/track/6yzHKyNLHZQDZzTuQrRF0G',
                    'https://open.spotify.com/track/5ONOlTiqymhzwcFjqcIT6E',
                    'https://open.spotify.com/track/5PyDJG7SQRgWXefgexqIge',
                    'https://open.spotify.com/track/7ArVzlFsFsQXNseVXmdOyk',
                    'https://open.spotify.com/track/0bYVPJvXr8ACmw313cVvhB',
                ]
                random.shuffle(song_urls)
                for _ in range(3 - len(Queue.query.all())):
                    for song_url in song_urls:
                        if song_url not in bad_song_urls:
                            bad_song_urls.append(song_url)
                            db.session.add(Queue(song_url=song_url, score=1, rawscore=random.uniform(0.5, 1), multiplier=1, timestamp=now))
                            db.session.commit()
                            break
                    else:
                        app.logger.warning('Failed to find a single new recommendation not already selected!')

            # Update queue scores based on new vibe and decay
            for entry in Queue.query.all():
                song = SpotifySong.get(entry.song_url)
                entry.multiplier = 1 + sum([genres[genre] for genre in song.genres.split('\t') if genre in genres])
                entry.multiplier += min(1, max(0, 1 - abs(average_acousticness - song.acousticness)))
                entry.multiplier += min(1, max(0, 1 - abs(average_danceability - song.danceability)))
                entry.multiplier += min(1, max(0, 1 - abs(average_energy - song.energy)))
                entry.multiplier += min(1, max(0, 1 - abs(average_valence - song.valence)))
                entry.score = (entry.rawscore - (now - entry.timestamp) / 600) * entry.multiplier
            db.session.commit()

        except TimeoutError:
            delay = 15

        delay = min(15, delay + 0.25)
        app.logger.info(f'RESTing for {delay}s...')
        time.sleep(delay)
