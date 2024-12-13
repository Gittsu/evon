import os
import webbrowser
from datetime import datetime
from src.utils import speak  # Import speak from utils.py

def handle_command(command):
    """
    Processes the command and performs the corresponding actions.
    """
    if "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")
    elif "open browser" in command:
        speak("Opening your default web browser.")
        webbrowser.open("https://www.google.com")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}.")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    elif "play music" in command:
        music_dir = "D:\\Music"  # Replace with your music folder path
        try:
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing music.")
            else:
                speak("No music files found in the directory.")
        except FileNotFoundError:
            speak("Music directory not found. Please update the path.")
    else:
        speak("Sorry, I don't know how to do that yet.")
