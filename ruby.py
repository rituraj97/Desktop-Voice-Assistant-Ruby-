import pyttsx3                                          #pip install pyttsx3
import speech_recognition as sr                         #pip install speechRecognition
import datetime
import wikipedia                                        #pip install wikipedia
import webbrowser
import os
import smtplib
import socket, threading
import sys

class DevNull:
        def write(self, msg):
                pass
                
sys.stderr = DevNull()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice', voices[1].id)

#chatapp
def accept_client():
        while True:
                #accept    
                cli_sock, cli_add = ser_sock.accept()
                CONNECTION_LIST.append(cli_sock)
                thread_client = threading.Thread(target = broadcast_usr, args=[cli_sock])
                thread_client.start()

def broadcast_usr(cli_sock):
        while True:
                try:
                        data = cli_sock.recv(20801)
                        if data:
                           b_usr(cli_sock, data)
                except Exception as x:
                        print(x.message)
                        break

def b_usr(cs_sock, msg):
        for client in CONNECTION_LIST:
                if client != cs_sock:
                        client.send(msg)

#assistant
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

        speak("I am Ruby Sir. Please tell me how may I help you")
        print("1. Open wikipedia(followed by the term to be searched on wikipedia)")
        print("2. Open chat application")
        print("3. Share file")
        print("4. Open google.com")
        print("5. Open stackoverflow.com")
        print("6. Open youtube.com")
        print("7. Play music")
        print("8. What's the time?")
        print("9. Send email")
        print("10. Quit Application")

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
                speak(f"User said: {query}")

        except Exception as e:
                #print(e)    
                print("Say that again please...")  
                return "None"
        return query

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('saurabhrituraj04@gmail.com', 'omruwhvyijzrphur')
        server.sendmail('saurabhrituraj04@gmail.com', to, content)
        server.close()

if __name__ == "__main__":
        wishMe()
        while True:
                query = takeCommand().lower()
                #query = 'open chat application'
                if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=4)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                elif 'open youtube' in query:
                        speak("Opening Youtube.com")
                        webbrowser.open("youtube.com")

                elif 'open chat application' in query:
                        speak("Opening command line based chat application")
                        CONNECTION_LIST = []

                        # socket
                        ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                        # bind
                        HOST = 'localhost'
                        PORT = 3000
                        ser_sock.bind((HOST, PORT))

                        #listen    
                        ser_sock.listen(1)
                        print('Chat server started on port : ' + str(PORT))

                        thread_ac = threading.Thread(target = accept_client)
                        thread_ac.start()
                        os.system("start cmd /c Python C:\\--path-to-\\client.py")
                        os.system("start cmd /c Python C:\\--path-to-\\client.py")
                        os.system("pause")
                        ser_sock.close()
                                                
                elif 'share file' in query:
                        speak("Looking for a client to share files with")
                        CONNECTION_LIST = []
                        # socket
                        ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        # bind
                        HOST = localhost
                        PORT = 3000
                        ser_sock.bind((HOST, PORT))
                        #listen    
                        ser_sock.listen(1)
                        print(HOST)
                        print("Waiting for any incoming connections ... ")
                        os.system("start cmd /c Python C:\\--path-to-\\fileclient.py")
                        conn, addr = ser_sock.accept()
                        speak(f"{addr} Has connected to the server")
                        filename = input(str("Please enter the filename of the file : "))
                        file = open(filename , 'rb')
                        file_data = file.read(99999999)
                        conn.send(file_data)
                        os.system("pause")
                        print("Data has been transmitted successfully")


                elif 'open google' in query:
                        speak("Opening Google.com")
                        webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                        speak("Opening stackoverflow.com")
                        webbrowser.open("stackoverflow.com",new=0)   


                elif 'play music' in query:
                        music_dir = "C:\\--path-to\\songs"
                        songs = os.listdir(music_dir)
                        print(songs)    
                        os.startfile(os.path.join(music_dir, songs[1]))

                elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                        speak("Sir, the time is " + strTime)

                elif 'thanks' in query:
                        speak("Thanks for using. Good Bye! Take Care! quitting!!")
                        exit(0)
                elif 'exit' in query:
                        speak("Thanks for using. Good Bye! Take Care! quitting!!")
                        exit(0)

                elif 'send email' in query:
                        try:
                                speak("Enter email address")
                                to = input("Enter email address here.. @: ")
                                speak("What should I say?")
                                content = takeCommand()  
                                sendEmail(to, content)
                                speak("Email has been sent!")
                        except Exception as e:
                                print(e)
                                speak("Sorry my friend. I am not able to send this email")
                elif 'about you' in query:
                        speak("I am ruby, your system assistant. i was developed by Rituraj Saurabh and Salini Binu as their mini project of computer networks paper.")
                        speak("I understand following commands:")
                        print("1. Open wikipedia(followed by the term to be searched on wikipedia)")
                        print("2. Open chat application")
                        print("3. Share files")
                        print("4. Open google.com")
                        print("5. Open stackoverflow.com")
                        print("6. Open youtube.com")
                        print("7. Play music")
                        print("8. What's the time?")
                        print("9. Send email")
                        print("10. Quit Application")
                        speak("Open wikipedia")
                        speak("Open chat application")
                        speak("share files")
                        speak("open google")
                        speak("open stackoverflow")
                        speak("open youtube")
                        speak("play music")
                        speak("what's the time")
                        speak("send email")
                        speak("quit application")
                        
                else:
                        speak("i don't know. try something else!")
