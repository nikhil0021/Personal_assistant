import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os

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
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak('According to wikipedia')

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')

        elif 'open gmail' in query:
            webbrowser.open('https://mail.google.com/mail/?tab=rm')

        elif 'play music' in query:
            music = 'C:\\Users\\HP\\Music'
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {time}')

        elif 'study folder' in query:
            path = 'E:\\study\\sem8'
            os.startfile(path)

        elif 'quit' in query:
            exit()
