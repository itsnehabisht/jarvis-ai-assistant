from speak import speak
from actions import *

def handle_command(command):
    command = command.lower()

    if command == "hello" or command == "hi jarvis":
        speak("Hello! How can I help you?")

    elif command == "what is the time":
        tell_time()

    elif "open youtube" in command:
        speak("Opening YouTube")
        open_website("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        open_website("https://google.com")

    else:
        speak("I did not understand your command")