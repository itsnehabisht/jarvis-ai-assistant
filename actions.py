import datetime
import webbrowser
import urllib.parse
import os
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


def google_search(query):
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    speak(f"Searching Google for {query}")
    webbrowser.open(url)


def open_application(app):
    speak(f"Opening {app}")
    os.system(f"start {app}")
