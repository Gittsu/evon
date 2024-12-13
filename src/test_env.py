import sys
import os
import speech_recognition as sr
from src.utils import speak  # Import speak from utils.py
from src.command_handler import handle_command  # Import handle_command from command_handler.py

# Add the root directory (parent of src) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def recognize_speech():
    """
    Recognizes speech input from the microphone and returns the command as text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Could not connect to the recognition service.")
            return None
        except sr.WaitTimeoutError:
            speak("No command detected.")
            return None

if __name__ == "__main__":
    speak("Hello, I am Evon. How can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            handle_command(command)
