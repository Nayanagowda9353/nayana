from flask import Flask, render_template, send_file, abort, Response, redirect
import os

app = Flask(__name__)

# Path to the music directory
MUSIC_DIR = os.path.join(app.root_path, 'static', 'music')

# Sample music tracks metadata (id, title, url)
tracks = [
    {'id': '1', 'title': 'Sample Track 3', 'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3'},
    {'id': '2', 'title': 'Sample Track 4', 'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3'},
    {'id': '3', 'title': 'Sample Track 5', 'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3'},
    {'id': '4', 'title': 'Sample Track 6', 'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3'},
]

@app.route('/')
def index():
    return render_template('index.html', tracks=tracks)

@app.route('/play/<track_id>')
def play(track_id):
    track = next((t for t in tracks if t['id'] == track_id), None)
    if not track:
        abort(404)
    return render_template('player.html', track=track)

@app.route('/stream/<track_id>')
def stream(track_id):
    track = next((t for t in tracks if t['id'] == track_id), None)
    if not track:
        abort(404)
    # Redirect to external URL for streaming
    return redirect(track['url'])

if __name__ == '__main__':
    app.run(debug=True)
