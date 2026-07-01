import datetime
import webbrowser
from speak import speak

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I %M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    today = datetime.datetime.now()
    date = today.strftime("%d %B %Y")
    speak(f"Today's date is {date}")

    
def open_website(name, url):
    speak(f"Opening {name}")
    webbrowser.open(url)