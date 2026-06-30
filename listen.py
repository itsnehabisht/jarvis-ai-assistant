import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        audio = recognizer.listen(source)


    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text


    except:

        print("Could not understand")

        return ""
