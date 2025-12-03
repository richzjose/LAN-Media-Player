from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
SONG_DIR = "songs"

@app.route("/")
def index():
    return send_from_directory(".", "client.html")

@app.route("/list")
def list_songs():
    files = [f for f in os.listdir(SONG_DIR)
             if f.lower().endswith((".mp3", ".wav", ".ogg"))]
    return jsonify(files)

@app.route("/audio/<path:filename>")
def audio(filename):
    return send_from_directory(SONG_DIR, filename)

if __name__ == "__main__":
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()

    print("Open on your phone:")
    print(f"http://{host}:5000")
    app.run(host="0.0.0.0", port=5000)
