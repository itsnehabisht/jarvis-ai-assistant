from listen import listen
from commands import handle_command


while True:

    command = listen()
    print(f"You said: {command}")
    if command:
        handle_command(command)