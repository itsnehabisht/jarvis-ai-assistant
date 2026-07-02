from speak import speak
from actions import tell_time, tell_date, open_website, google_search, open_application

def handle_command(command):
    command = command.lower().strip()

    print("Processing command:", command)

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "open youtube" in command:
        open_website("youtube", "https://youtube.com")

    elif "open google" in command:
        open_website("google", "https://google.com")

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            google_search(query)
        else:
            speak("Please provide a search query.")

    elif "open calculator" in command:
        open_application("calc")

    elif "open notepad" in command:
        open_application("notepad")

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        exit()

    else:
        speak("I did not understand your command")