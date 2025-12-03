# 📀 LAN Music Player
A lightweight local-network music streaming app that lets you play songs stored on your computer directly from any device on the same Wi-Fi network.

This project uses a Flask backend to serve audio files and a modern, glass-style HTML/JS frontend that provides a responsive, touch-friendly music player interface.

# ✨ Features
🎵 Stream Local Songs Over LAN
Open the link on your phone, tablet, or another computer to play audio files stored on your PC.

📁 Automatic Playlist Generation
Scans the /songs folder and lists all .mp3, .wav, and .ogg files.

▶️ Full Playback Controls

Play / Pause

Next / Previous

Tap any song to start playing

Seek progress bar

🎚️ Animated Visualizer
Smooth bar animation for a lively music player UI.

# 🚀 How It Works
1. Backend (Flask)

The Python server:

>Serves the HTML UI

>Lists available songs from /songs

>Streams audio files to connected devices

2. Frontend (HTML/CSS/JS)

The client page:

>Fetches song list

>Plays audio via <audio> element

>Handles playback controls, UI animations, seeking, and active state


📱 Mobile-Friendly
Designed to work perfectly on phones.


🧪 Usage

Put music files into the songs/ folder

Run:
python server.py


On startup, you’ll see something like:

Open on your phone:
http://192.168.x.x:5000



📌 Requirements

Python 3
Flask
Local network connection (same Wi-Fi)

Open that link on your phone and enjoy!

