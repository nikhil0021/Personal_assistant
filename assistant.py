import datetime
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak('Good morning darling!!')
    elif 12 < hour < 16:
        speak('Good afternoon darling!!')
    elif 15 < hour < 18:
        speak('Good evening master!!')
    else:
        speak('Good night dear!!')
    speak('What can i do for you my lord?')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception:
        print('Sorry. I can\'t understood what you said\n Please say it again!!')
        return 'None'
    return query


if __name__ == '__main__':
    wishme()
    takecommand()
