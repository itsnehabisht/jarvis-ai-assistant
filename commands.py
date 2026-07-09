from speak import speak
from actions import (
    tell_time,
    tell_date,
    open_website,
    google_search,
    open_application,
)
from ai import ask_ai
from weather import get_weather


def handle_command(command):
    command = command.lower().strip()

    # Greetings
    if command in ["hi", "hello"]:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        tell_time()

    # Date
    elif "date" in command:
        tell_date()

    # Open websites
    elif "open youtube" in command:
        open_website("YouTube", "https://youtube.com")

    elif "open google" in command:
        open_website("Google", "https://google.com")

    # Google Search
    elif "search" in command:
        query = command

        words_to_remove = {
            "search",
            "for",
            "please",
            "can",
            "you",
            "ok",
            "okay",
            "then",
        }

        query = " ".join(
            word for word in query.split()
            if word not in words_to_remove
        )

        if query:
            google_search(query)
        else:
            speak("Please tell me what you want to search.")

    # Open Applications
    elif "open calculator" in command:
        open_application("calc")

    elif "open notepad" in command:
        open_application("notepad")

    # Weather
    elif "weather" in command:

        words_to_remove = {
            "what",
            "is",
            "what's",
            "tell",
            "me",
            "show",
            "the",
            "weather",
            "in",
            "of",
    }

        city = " ".join(
            word for word in command.split()
            if word not in words_to_remove
        )

        if city:
            weather = get_weather(city)
            speak(weather)
        else:
            speak("Please tell me the city name.")

    # Exit
    elif "stop" in command or "bye" in command or "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    # AI
    else:
        response = ask_ai(command)
        speak(response)