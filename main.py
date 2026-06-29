import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone:
        audio = recognizer.listen(microphone)


    try:
        text = recognizer.recognize_google(audio)
        return text
    except:
        return "Sorry, I could not understand what you said."
    
command = listen()

if command == "hello":
    speak("Hello! How can I help you?")
else:
    speak("I did not understand")

# print(f"You said: {command}")
