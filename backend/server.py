from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import waitress
import logging


app = Flask(__name__)
app.config['SECRET_KEY'] = 'todo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ContextLogger(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f'{self.extra} | {msg}', kwargs


class LeaderboardSong(db.Model):
    uri = db.Column(db.String(64), nullable=False, primary_key=True)
    score = db.Column(db.Float, nullable=False, default=1.0)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class HistorySong(db.Model):
    uri = db.Column(db.String(64), nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


@app.route('/status', methods = ['GET'])
def get_status():
    log = ContextLogger(app.logger, '/status')
    log.info('New request')

    # TODO: pull data from database
    # LeaderboardSong.query.all()

    return {
        'current': {
            'uri': 'uri',
            'track': 'track',
            'album': 'album',
            'albumart': 'albumart',
            'artist': 'artist',
            'length': 0.0
        },
        'leaderboard': [
            {
                'uri': 'uri1',
                'track': 'track1',
                'album': 'album1',
                'albumart': 'albumart1',
                'artist': 'artist1',
                'length': 0.0,
                'rawscore': 0.0,
                'multipler': 1.0,
            },
            {
                'uri': 'uri2',
                'track': 'track2',
                'album': 'album2',
                'albumart': 'albumart2',
                'artist': 'artist2',
                'length': 0.0,
                'rawscore': 0.0,
                'multipler': 1.0,
            },
        ],
        'vibe': {
            'rock': 15,
            'punk': 12,
            'jazz': 3,
        },
    }


@app.route('/analytics', methods = ['GET'])
def get_analytics():
    log = ContextLogger(app.logger, '/analytics')
    log.info('New request')

    # TODO: pull data from database
    return {
        'todo': 'no idea what to put here yet'
    }


@app.route('/vote', methods = ['POST'])
def post_vote():
    log = ContextLogger(app.logger, '/vote')
    log.info('New request')

    uri = request.args.get('uri')
    if uri is None or uri == '':
        log.warning('Missing URI')
        return { 'err': 'Missing URI'}, 400

    try:
        session.permanent = True
        time = float(session[uri])
        log.info(f'Previous vote time: {time}')
    except (KeyError, ValueError):
        log.info('No previous vote found')
        time = 0

    now = datetime.utcnow().timestamp()
    if time > now - 3600: # More than 1 hour ago?
        log.info('Rejected duplicate vote')
        return {'err': 'Voted for URI too recently'}, 403
    session[uri] = now

    log.info('TODO: handle new valid vote')
    # TODO: cast vote into database, update queue, etc
    # foo = LeaderboardSong(uri='test_song2')
    # db.session.add(foo)
    # db.session.commit()

    # returns new values
    return {'rawscore': 0.0, 'multipler': 1.0}


with app.app_context():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[logging.FileHandler('instance/output.log'), logging.StreamHandler()])
    db.create_all()
    waitress.serve(app, host='0.0.0.0', port=8080)
