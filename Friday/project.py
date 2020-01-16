import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('54WKH5-86QY224A93')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    print('Friday: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning boss!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon boss!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening boss!')


greetMe()

speak('what do you need?')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')


    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))


    return query


if __name__ == '__main__':

    while True:
        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "how are you" in query or 'what up?' in query:
            stMsgs = ['I am fine thank you ! ','awesome','all good']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What you want to say?')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("ofirlly65@gmail.com", 'o168010200')
                    server.sendmail('ofirlly65@gmail.com','ofirlly65@gmail.com',content)
                    server.quit()
                    speak('Email sent!')
                except:
                    speak('Sorry boss! I couldnt send your email this time!')


        elif 'nothing' in query  or 'stop' in query or 'bye' in query:
            speak('okay...until next time...bye boss!')
            sys.exit()

        elif 'friday' in query or 'hello' in query or 'hey' in query:
            speak('hey boss')
        elif 'who are you' in query:
            speak('I am your digital assistant Friday...i was born in january 16th 2020...your wish is my commend')


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('well...')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('well...')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak("what's next boss?")
