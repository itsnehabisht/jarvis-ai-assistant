from speak import speak
from listen import listen
from commands import handle_command

awake = False

while True:

    command = listen()

    if not command:
        continue

    command = command.lower().strip()

    if awake:

        if command == "sleep" or command == "go to sleep":
            awake = False
            speak("Going to sleep.")

        else:
            if "hey jarvis" in command:
                command = command.replace("hey jarvis", "").strip()

            handle_command(command)


    else:
    
        if "hey jarvis" in command:
            awake = True
            command = command.replace("hey jarvis", "").strip()

            if command=="":
                speak("Hello. How can I assist you?")

            else:
                handle_command(command)
    
        else:
            continue