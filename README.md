🎥 AI Voice Assistant with Video Playback


This Python project integrates speech recognition, text-to-speech, and Generative AI to create an interactive voice assistant that listens to your voice commands, responds using Google's Gemini API, and continuously plays a looping video in a separate window.

🧠 Features
🎙️ Voice Command Input using speech_recognition

🗣️ AI-Powered Responses using Google Gemini API

🔊 Spoken Replies using pyttsx3

📺 Continuous Video Playback using OpenCV

🧵 Multithreaded for simultaneous listening and video playing

🛠️ Requirements
Install the required libraries using pip:
pip install opencv-python speechrecognition pyttsx3 google-generativeai

📁 Project Structure

├── main.py                # Main program file
├── config.json            # API key configuration file
├── newth.mp4              # Video file to be played in a loop
└── README.md              # This file

🔑 Configuration
Create a config.json file in the project directory with the following format:

json

{
  "api_key": "YOUR_GEMINI_API_KEY_HERE"
}
💡 Replace "YOUR_GEMINI_API_KEY_HERE" with your actual API key from Google Generative AI.

▶️ Running the Project
Make sure newth.mp4 is present in the directory.

Run the main script:


python main.py
Speak into your microphone. The assistant will respond to your queries.

Say "exit" or "stop" to terminate the program.

❗ Notes
Press q on the video window to close the video playback.

Ensure your microphone is enabled and accessible.

The assistant uses a female voice by default.

