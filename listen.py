import speech_recognition as sr

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