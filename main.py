from listen import listen
from commands import handle_command


while True:

    command = listen()
    handle_command(command)