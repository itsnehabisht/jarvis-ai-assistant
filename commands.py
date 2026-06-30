from speak import speak
from actions import tell_time, tell_date, open_website

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
        speak("Opening YouTube")
        open_website("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        open_website("https://google.com")

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        exit()

    else:
        speak("I did not understand your command")