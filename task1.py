import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import emoji #pip install emoji

print("-----------------------WELCOME------------------------")
print(emoji.emojize(" Here,some menu that program helps you to launched:red_heart:",variant="emoji_type"))





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):   
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Curie Mam. Please tell me how may I help you")
    speak("Here,some menu that program helps you to launched easily")
    
    print(" 1.Open Notepad\n 2.Open Chrome\n 3.Open VLC player\n 4.Search Wikipedia \n 5.Open Paint\n 6.Open youtube\n 7.Send E-mail to someone \n 8.Play Music \n 9.Open Stackoverflow to search\n 11.Current time\n 12.Open Google\n 13.Exit\n") 



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
         
        return "None"
    return query 



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('prachisingh.mbd123@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak(f"We are launching your request of {query} please wait.....")
            os.system(" chrome youtube.com")

        elif 'google' in query:
            speak(f"We are launching your request of {query} please wait.....")
            os.system(" chrome google.com")

        elif 'stack overflow' in query:
            speak(f"We are launching your request of {query} please wait.....")
            os.system(" chrome stackoverflow.com")   


        elif 'music' in query:
            speak(f"We are launching your request of {query} please wait.....")
            music_dir = 'C:\\Users\\user\\Music\\fav'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")

        elif 'send email' in query:
            try:
                speak("What should  I write for message?")
                content = takeCommand()
                speak("To whom you want to send")
                to = input("To whom you want to send,please enter email")    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry , I am not able to send this email")  
        elif 'notepad' in query:
            speak(f"We are launching your request of {query} please wait...")
            os.system("notepad")
        elif 'vlc player' in query:
            pyttsx3.speak(f"We are launching your request of {query} please wait...")
            os.system("VLC")
        elif 'paint' in query:
            speak(f"We are launching your request of {query} please wait...")
            os.system("mspaint")
        elif 'chrome' in query:
            speak(f"We are launching your request of {query} please wait...")
            os.system("chrome")
        

        elif 'exit' in query:
            speak("Exiting Mam, Thank you for using Program, have a nice day ")
            break   

        



