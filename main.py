from listen import listen
from commands import handle_command


while True:

    command = listen()
    
    if command:
        handle_command(command)