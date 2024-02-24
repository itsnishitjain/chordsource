from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import waitress
import logging

# TODO: be able to do something at end of song (or at least near end)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'todo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ContextLogger(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f'{self.extra} | {msg}', kwargs


class Leaderboard(db.Model):
    song_url = db.Column(db.String(128), db.ForeignKey('spotify_song.url'), nullable=False, primary_key=True)
    song = db.relationship('SpotifySong', backref=db.backref('leaderboard', uselist=False))
    rawscore = db.Column(db.Float, nullable=False, default=1.0)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class History(db.Model):
    song_url = db.Column(db.String(128), db.ForeignKey('spotify_song.url'), nullable=False, primary_key=True)
    song = db.relationship('SpotifySong', backref=db.backref('history', uselist=False))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class SpotifySong(db.Model):
    url = db.Column(db.String(128), nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    length = db.Column(db.BigInteger, nullable=False)
    album_url = db.Column(db.String(128), db.ForeignKey('spotify_album.url'), nullable=False)
    album = db.relationship('SpotifyAlbum', backref=db.backref('spotify_song', uselist=False))
    artist_url = db.Column(db.String(128), db.ForeignKey('spotify_artist.url'), nullable=False)
    artist = db.relationship('SpotifyArtist', backref=db.backref('spotify_song', uselist=False))


class SpotifyAlbum(db.Model):
    url = db.Column(db.String(128), nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    art = db.Column(db.String(128), nullable=False)


class SpotifyArtist(db.Model):
    url = db.Column(db.String(128), nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)


@app.route('/status', methods = ['GET'])
def get_status():
    log = ContextLogger(app.logger, '/status')
    log.info('New request')

    history = History.query.all()
    if len(history) == 0:
        current = None
    else:
        latest = history[0] # TODO: get most latest history (aka by date)
        current = {
            'url': latest.song.url,
            'track': latest.song.name,
            'album': latest.song.album.name,
            'albumart': latest.song.album.art,
            'artist': latest.song.artist.name,
            'length': latest.song.length,
            'date': latest.date,
        }

    leaderboard = []
    for entry in Leaderboard.query.all():
        leaderboard.append({
            'url': entry.song.url,
            'track': entry.song.name,
            'album': entry.song.album.name,
            'albumart': entry.song.album.art,
            'artist': entry.song.artist.name,
            'length': entry.song.length,
            'date': entry.date,
            'rawscore': entry.rawscore,
            'multipler': 1.0, # TODO: generate multiplier for song based on current genres
        })

    genres = {}
    for entry in history: # TODO: get 10 latest
        if entry.song.artist.genre in genres:
            genres[entry.song.artist.genre] += 1
        else:
            genres[entry.song.artist.genre] = 1

    return {
        'current': current,
        'leaderboard': leaderboard,
        'genres': genres,
    }


@app.route('/analytics', methods = ['GET'])
def get_analytics():
    log = ContextLogger(app.logger, '/analytics')
    log.info('New request')

    return {
        'todo': 'no idea what to put here yet'
    }


@app.route('/vote', methods = ['POST'])
def post_vote():
    log = ContextLogger(app.logger, '/vote')
    log.info('New request')

    url = request.args.get('url')
    if url is None or url == '':
        log.warning('Missing URL')
        return {'err': 'Missing URL'}, 400

    try:
        session.permanent = True
        time = float(session[url])
        log.info(f'Previous vote time: {time}')
    except (KeyError, ValueError):
        log.info('No previous vote found')
        time = 0

    now = datetime.utcnow().timestamp()
    if time > now - 3600: # More than 1 hour ago?
        log.info('Rejected duplicate vote')
        return {'err': 'Voted for URL too recently'}, 403
    session[url] = now

    log.info('TODO: handle new valid vote')
    # TODO: cast vote into database, update queue, etc
    # foo = LeaderboardSong(url='test_song2')
    # db.session.add(foo)
    # db.session.commit()

    # TODO: caching spotify song stuff goes here

    # returns new values
    return {'rawscore': 0.0, 'multipler': 1.0}


with app.app_context():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[logging.FileHandler('instance/output.log'), logging.StreamHandler()])
    db.create_all()
    waitress.serve(app, host='0.0.0.0', port=8080)
