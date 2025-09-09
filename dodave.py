#C:\Users\91767\Desktop\python\pythooon\dodave.py
import platform
import re
from re import search
#import processor
import sys
import pyjokes
#import pygame
#from pygame.locals import*
import pyttsx3
import datetime
import gtts as gtts #can be used instead of sapi5 for taking voice of google assistant
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import cv2
import mediapipe as mp
#import pywin32_system32                           -|---------\   for 'iron man mode'
#from pywin32_system32 import win32api             -|---------/
import pyautogui
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
#from dodave1 import Ui_MainWindow
from email.mime.text import MIMEText
import vlc    #allows u to play media files and control playback
#import youtube_search
import subprocess
import pytube
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# # IMPORTS FOR STARTING CHATBOX
# import threading
# from flask import Flask, render_template, request, jsonify
# from flask_socketio import SocketIO, emit
# import time
# import queue




'''#starting of app making
LOCATEF = "GALLERY/BG"
SCREENWIDTH = 1500
SCREENHEIGHT = 970
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENWIDTH))
BACKGROUND =  "LOCATEF/blueprint.jpeg"
GROUNDY = SCREENHEIGHT = 0.2
GAME_SPRITES = {}


if __name__ == "__main__":
    pygame.init() #uses all pygame module
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Jarvis by Publishingart")

#end of app making'''


engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 150)  # Set the speech rate to 150
engine.setProperty('volume', 1.0)  # Set the speech volume to 1.0
voices = engine.getProperty('voices')
#print(voices)
# engine.setProperty('voices', voices[3].id)
# engine.setProperty('voices')
engine.setProperty('voices', voices[1].id)


# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")


# ===== Global Settings =====
'''log_queue = queue.Queue()
mode = "voice"  # default mode

def add_chat(sender, text):
    """Push message to chat UI."""
    log_queue.put({"sender": sender, "text": text})'''

# mode = "text"
# listening = False
# command_queue = queue.Queue()

# chat_history = []

# def add_chat(sender, text):
#     chat_history.append({"sender": sender, "text": text})
#     socketio.emit('new_message', {"sender": sender, "text": text})



def speak(text, emotion):
    print(f"Jarvis: {text}")
    add_chat("Jarvis", text)
    if emotion == "happy":
        engine.setProperty('rate', 150)  # Set the speech rate to 150
        engine.setProperty('volume', 1.0)  # Set the speech volume to 1.0
    elif emotion == "loving":
        engine.setProperty('rate', 120)  # Set the speech rate to 120
        engine.setProperty('volume', 0.8)  # Set the speech volume to 0.8
    elif emotion == "angry":
        engine.setProperty('rate', 180)  # Set the speech rate to 180
        engine.setProperty('volume', 1.2)  # Set the speech volume to 1.2
    elif emotion == "confused":
        engine.setProperty('rate', 150)  # Set the speech rate to 150
        engine.setProperty('volume', 1.0)  # Set the speech volume to 1.0
    elif emotion == "sad":
        engine.setProperty('rate', 100)  # Set the speech rate to 100
        engine.setProperty('volume', 0.6)  # Set the speech volume to 0.6
    elif emotion == "obedient":
        engine.setProperty('rate', 130)  # Set the speech rate to 130
        engine.setProperty('volume', 0.9)  # Set the speech volume to 0.9
    elif emotion == "sleepy":
        engine.setProperty('rate', 90)  # Set the speech rate to 90
        engine.setProperty('volume', 0.7)  # Set the speech volume to 0.7




    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Mornning Boss", "happy")
        print("Good Mornning Boss")

    elif hour == 12 :
        speak("Good nooon Boss", "happy")
        print("Good nooon Boss")


    elif hour>=22 or hour<6:
        speak("Boss any important work late night", "sleepy")
        print("Boss any important work late night")

    elif hour> 12 and hour<17:
        speak("good afternooon Boss", "obedient")
        print("good afternooon Boss")

    elif hour> 17 and hour<22:
        speak("Good Eveninng Boss", "obedient")
        print("Good Eveninng Boss")
        
    speak("Please tell me how can I help you", "obedient")
    print("Please tell me how can I help you")

def takeCommand():
    # global mode
    # #Takes command/microphone input and give us string command
    # if mode == "text":
    #     # Wait until text command is received via web
    #     while True:
    #         try:
    #             #cmd_data = log_queue.get(timeout=0.1)
    #             cmd_data = command_queue.get(timeout=0.1)
    #             if cmd_data.get("type") == "web_command":
    #                 add_chat("You", cmd_data["text"])
    #                 return cmd_data["text"]
    #         except queue.Empty:
    #             pass
    # else:
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
         print("RecogniZing.....")
         query = r.recognize_google(audio, language='en-in')
         print(f"You said: {query}\n")
         #speak(f"You said: {self.query}\n")

    except Exception as e:
         print(e)
         print("say that again please.....")
         speak("say that again please.....", "confused")
         return "None"
    return query

#FOR EMAIL ID###################################
def validate_email(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email) is not None


with open('C:\\Users\\Admin\\Desktop\\pratham\\py tomb\\pythooon\\store_everything\\env_vars.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

password = os.environ['EMAIL_PASSWORD']

def sendEmail(to, subject, content): #pratham
    try:
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = 'prathamgoyal7411@gmail.com'
        msg['To'] = to

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('prathamgoyal7411@gmail.com', password)
        server.sendmail("prathamgoyal7411@gmail.com", to, msg.as_string())
        server.close()
        print("Boss email is sent!")
        speak("Boss email is sent!", "obedient")
    except smtplib.SMTPException as e:
        print("Error sending email:", e)
        speak("Error sending email:", e, "confused")

def send_email():
    try:
        speak("Do you want to speak or type the email address you want to send to?", "obedient")
        choice = takeCommand().lower()
        if 'speak' in choice or 'voice' in choice:
            speak("Please speak the email address you want to send to.", "obedient")
            to = takeCommand().lower()
            if not validate_email(to):
                speak("Invalid email address. Please try again.", "obidient")
                print("Invalid email address. Please try again.")
                return
        elif 'type' in choice or 'text' in choice:
            to = input("Please type the email address you want to send to: ")
            if not validate_email(to):
                speak("Invalid email address. Please try again.", "obidient")
                print("Invalid email address. Please try again.")
                return
        '''else:
            speak("Sorry, I didn't understand your choice. Please try again.", "confused")
            return'''
        
        speak("What should be the **subject** of the email?", "obedient")
        subject = takeCommand().upper()
        
        speak("What should I say in the email?", "obedient")
        content = takeCommand()
        print(content)
        
        sendEmail(to, subject, content)
    except Exception as e:
        print(e)
        speak("Sorry, I was unable to send the email.", "confused")

###########################################################

#For Love #################################################
def love():
    try:
        speak("what is your name", "happy") # Speak with a happy tone
        print("what is your name")
        print("Do you want to speak or write your name.")
        choice = input("Enter v for voive and w for typing.")
        if 'v' in choice:
            print("Speak...")
            Lname = takeCommand()
        if 'w' in choice:
            Lname = input("Write...: ")
#        if 'Pratham' in Lname or 'pratham' in Lname:
#            speak("Boss You should behave You already have a wife", "angry") # Speak with an angry tone
#            print("Boss You should behave You already have a wife")
        elif Lname.replace(" ", "").isalpha():
            speak("Awww thank you Boss I love YOU too", "loving") # Speak with a loving tone
            print("Awww thank you Boss I love YOU too")
        else:
            speak("I could not hear your name can you pleaseeee repeate the name", "confused") # Speak with a confused tone
            print("I could not hear your name can you pleaseeee repeate the name")
            return
        
    except Exception as e:
        print(e)
        speak("I might not have heard your name, but I Love YOU", "sad") # Speak with a sad tone

###########################################################

#For Playing Song #########################################
def play_song(song_name, loop = False):
    music_folder = os.path.join(os.path.expanduser('~'), 'Music')
    playlist_folder = os.path.join(os.path.expanduser('~'), 'Playlist')

    # Search in playlist folder
    for root, dirs, files in os.walk(playlist_folder):
        for file in files:
            if song_name.lower() in files.lower():
                song_path = os.path.join(root, file)
                if loop:
                    vlc_instance = vlc.Instance()
                    media_player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new(song_path)
                    media.add_option("repeat")
                    media_player.set_media(media)
                    media_player.play()                  
                else:
                    os.startfile(song_path)
                print(f"Playing {song_name} from playlist...")
                return

    # Search in music folder
    for root, dirs, files in os.walk(music_folder):
        for file in files:
            if file.endswith (('.mp3', '.wav', '.ogg', '.m4a')):  #Add more file extension as needed
                if song_name.lower() in file.lower():
                    song_path = os.path.join(root, file)
                    if loop:
                        vlc_instance = vlc.Instance()
                        media_player = vlc_instance.media_player_new()
                        media = vlc_instance.media_new(song_path)
                        media.add_option("repeat")
                        media_player.set_media(media)
                        media_player.play()
                    else:
                        os.startfile(song_path)
                    print(f"Playing {song_name} from music folder...")
                    return
    
    print(f"Song {song_name} not found in playlist or music folder. Searching entire computer...")
    search_computer(song_name)

def search_computer(song_name, loop = False):
    for root, dirs, files in os.walk('C:\\Users\\Admin\\'):
        for file in files:
            if file.endswith(('.mp3', '.wav', '.ogg', '.m4a')):  # Add more file extensions as needed
                if song_name.lower() in file.lower():
                    song_path = os.path.join(root, file)
                    if loop:
                        vlc_instance = vlc.Instance()
                        media_player = vlc_instance.media_player_new()
                        media = vlc_instance.media_new(song_path)
                        media.add_option("repeat")
                        media_player.set_media(media)
                        media_player.play()
                    else:
                        os.startfile(song_path)
                    print(f"Found {song_name} on computer: {song_path}")
                    return

    print(f"Song {song_name} not found on computer. Searching on youtube ")
    play_on_yt(song_name)

def search_youtube(song_name):
    """
    Search for a YouTube video by name.
    
    Args:
        song_name (str): The name of the song to search for.
    
    Returns:
        str: The URL of the first search result.
    """

    '''scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        q=song_name,
        type="video",
    )
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        item = response['items'][0]
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    else:
        speak("No results found on YouTube.", "confused")
        return None'''
    
    '''url = f"https://www.youtube.com/results?search_query={song_name}"
    vids = webbrowser.search_youtube(url, max_results=1)
    video_url = f"https://www.youtube.com/watch?v={vids[0]['id']}"
    return video_url'''
    # Craet a YouTube object
    yt = pytube.YouTube()

    # Search for Videos
    videos = yt.search(song_name)

    # Get the first video result
    video = videos[0]

    # Get the Video URL
    video_url = video.watch_url

    return video_url
 
def play_on_yt(video_url, loop = False):
    

    """video_url= search_youtube(song_name)
    webbrowser.open(video_url)
    print(f"Playing {song_name} on YouTube...")"""
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(video_url)
    player.set_media(media)
    player.play()

    if loop:
        while True:
            print("Looping YouTube search...")
            time.sleep(10)
            webbrowser.execute_script("window.location.reload();")

###########################################################

# To generate Image using AI ##############################
def generate_image():
    # get the text input from the operator
    speak("Enter the text to generate the image", "obidient")
    text = input("Enter the text to generate the image:")
    
    # Generate the ASCII art image using img2text
    #subprocess.run(["img2txt", "-w", "200", "-f", "slant", "-o", "generated_image.txt"], input = text.encode())
    with open("generated_image.txt", "w") as f:
        f.write(text)  # Simple placeholder for ASCII conversion

    # Open the generated image in the default text editor
    #subprocess.run(["gedit", "generated_image.txt"]) #### GEDIT is LINUX friendly
    subprocess.run(["notepad", "generated_image.txt"])

    # Ask the  operator if they are satisfied with the generated image
    speak("Are you satisfied with the image, boss? yes or no", "obidient")
    response = input("Are you satisfied with the image? (Yes/No)")
    if response.lower() == "no":
        print("Okay, let's generate a new image.")
        speak("Okay, Let's generate a new image", "sad")
        generate_image()

###########################################################




'''
#################################################
# for App interface
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Task()




class DNALikeItem(QtWidgets.QGraphicsItem):
    def __init__(self, parent=None):
        super(DNALikeItem, self).__init__(parent)
        self._rotation = 0.0

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 100, 100)

    def paint(self, painter, option, widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
        painter.drawEllipse(0, 0, 100, 100)

    def get_rotation(self):
        return self._rotation

    def set_rotation(self, value):
        self._rotation = value
        self.update()

    rotation = QtCore.pyqtProperty(float, get_rotation, set_rotation)

class AnimatableObject(QtCore.QObject):
    def __init__(self, dna_item):
        super(AnimatableObject, self).__init__()
        self.dna_item = dna_item
        self._rotation = 0.0

    def get_rotation(self):
        return self._rotation

    def set_rotation(self, value):
        self._rotation = value
        self.dna_item.setRotation(value)

    rotation = QtCore.pyqtProperty(float, get_rotation, set_rotation)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.scene = QtWidgets.QGraphicsScene(self)
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        self.dna_item = DNALikeItem()
        self.scene.addItem(self.dna_item)

        self.animatable_object = AnimatableObject(self.dna_item)
        self.animation = QtCore.QPropertyAnimation(self.animatable_object, b"rotation")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(360)
        self.animation.setLoopCount(-1)
        self.animation.start()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton("Push Button")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        
        


        self.pushButton_exit = QtWidgets.QPushButton("Exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.pushButton_exit)  # Add the new exit button


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.scene = QtWidgets.QGraphicsScene(self)
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        self.dna_item = DNALikeItem()
        self.scene.addItem(self.dna_item)

        self.animatable_object = AnimatableObject(self.dna_item)
        self.animation = QtCore.QPropertyAnimation(self.animatable_object, b"rotation")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(360)
        self.animation.setLoopCount(-1)
        self.animation.start()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.ui.pushButton_exit.clicked.connect(self.on_pushButton_exit_clicked)


    def on_pushButton_clicked(self):
        print("Button clicked!")

    def on_pushButton_exit_clicked(self):
        print("Exit button clicked!")
        self.close()  # Close the main window


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################





class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)

    def startTask(self):
        main_thread = MainThread()
        main_thread.start()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task()

    def Task(self):
'''

# def JarvisMain():
wishMe()  # Call wishMe() only once at the beginning
while True:
    query = takeCommand().lower()
    #logic for executing this command based on qury (task)
    if 'wikipedia' in query:
        speak("searching for Request...", "obedient")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("Sir according to wikipedia", "obedient")
        speak(results, "obedient")
        print(results)
    elif 'your name' in query:
        speak("My name is Jarvis", "happy")
        print("My name is Jarvis")
    elif 'who is your creator' in query or 'who created you' in query:
        speak("my creator's name is Pratham", "loving")
        print("my creator's name is Pratham")
    elif 'open youtube' in query:
        speak("OK Boss opening YOUTUBE", "obedient")
        webbrowser.open("www.youtube.com")
    elif 'open google' in query:
        webbrowser.open("www.google.com")
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {strTime}", "obedient")
        print(f"sir, the time is {strTime}")
    elif 'what can i call you' in query or 'who are you' in query:
        speak('you can call me with any name boss', "loving")
    # for playing songs 
    elif 'play'in query:
        song_name = query.replace('play', '').strip()
        print(f"Searching for the {song_name}...")
        print("Is this the correct song? (Yes/No)")
        speak("Is this the correct song? Yes or No", "happy")
        response = takeCommand().lower()
        if response == 'no':
            speak("Please type the correct song name:", "obidiently")
            print("Please type the correct song name:")
            typed_song_name = input("Enter the song name: ")
            play_song(typed_song_name)
            print("Do you want to loop this song? (Yes/No)")
            speak("Do you want to loop this song? Yes or No", "happy")
            loop_response = takeCommand().lower()
            if loop_response == 'yes':
                play_song(typed_song_name, loop = True)
            elif loop_response == 'no':
                play_song(typed_song_name)
        elif response == ' yes':
            play_song(song_name)
            print("Do you want to loop this song? (Yes/No)")
            speak("Do you want to loop this song? Yes or No", "happy")
            loop_response = takeCommand().lower()
            if loop_response == 'yes':
                play_song(song_name, loop = True)
            elif loop_response == 'no':
                play_song(song_name)
        '''else:
            print("Do you want to loop this song? (Yes/No)")
            speak("Do you want to loop this song? Yes or No")
            if loop_response == 'yes':
                play_song(song_name, loop = True)
            else:
                print("Do you want to loop the playlist? (Yes/No)")
                playlist_loop_response = takeCommand().lower()
                if playlist_loop_response == 'yes':
                    #Loop the Playlist
                    playlist_folder = ''
                    for root, dirs, files in os.walk(playlist_folder):
                        for file in files:
                            if file.endswith(('.mp3', '.wav', '.ogg', '.m4a')): # Add new extensions if u have any
                                song_path = os.path.join(root, file)
                                vlc_instance = vlc.Instance()
                                media_player = vlc_instance.media_player_new()
                                media = vlc_instance.media_new(song_path)
                                media.add_option("repeat")
                                media_player.set_media(media)
                                media_player.play()'''
            
    elif 'search song named' in query:
        search_query = query.replace('search song named', '').strip()
        print(f"Searching for {search_query}...")
        confirm_search_song = takeCommand().lower()
        print("Is this the correct song? (Yes/No)")
        speak("Is this the correct song? Yes or No", "happy")
        if confirm_search_song == 'yes':
            play_song(search_query)
            print("Do you want to loop this song? (Yes/No)")
            speak("Do you want to loop this song? Yes or No", "happy")
            loop_response1 = takeCommand().lower()
            if loop_response1 == 'yes':
                play_song(search_query, loop = True)
            elif loop_response1 == 'no':
                play_song(search_query)

        elif confirm_search_song == 'no':
            speak("Please enter the correct search song:", "happy")
            print("Please enter the correct search song:")
            correct_search_song = input("Enter the search song:")
            play_song(correct_search_song)
            print("Do you want to loop this song? (Yes/No)")
            speak("Do you want to loop this song? Yes or No", "happy")
            loop_response1 = takeCommand().lower()
            if loop_response1 == 'yes':
                play_song(correct_search_song, loop = True)
            elif loop_response1 == 'no':
                play_song(correct_search_song)


    elif "generate image" in query or "create image" in query:
        try:
            generate_image()
        except Exception as e:
            print(e)
            speak(f"sorry sir because of {e}\n", "confused")


        '''print("Do you want to loop the search? (Yes/No)")
        loop_resp = takeCommand().lower()
        if loop_resp == 'yes':
            search_computer(search_query, loop=True)
        else:
            search_computer(search_query)'''
        
    '''elif 'play my playlist' in query:
        music_dir = ''
        songs = os.listdir(music_dir)
        print(songs)'''
    
    '''elif 'open unacademy' in query:
        webbrowser.open("https://unacademy.com")
    elif 'open unacademy santosh sir class' in query:
        webbrowser.open("https://unacademy.com/@santoshbhatt915")
    elif 'open unacademy deepak sir class' in query:
        webbrowser.open("https://unacademy.com/@unacademy-user-0DGMDV4NSHIM")
    elif 'open whatsapp' in query:
        open("ww.whatsappweb.com")
    elif 'diksha mam class' in query:
        webbrowser.open("https://us04web.zoom.us/j/76236614263?pwd=WHZva2dFM3grOFZNZWp2S0tMaXdkZz09")
    elif 'Nidhi mam class' in query:
        webbrowser.open("https://us04web.zoom.us/j/77352329748")'''
    
    
    if 'open whatsapp'in query:
        try:
            codePath = "C:\\Users\\91767\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
        except:
            speak("As i am not able to locate the WhatsApp in your device and will open on your webbrowser now ")
            print("As i am not able to locate the WhatsApp in your device and will open on your webbrowser now ")
            whatsapp_url = "https://web.whatsapp.com/"
            webbrowser.open(whatsapp_url)    

    elif 'email' in query or 'letter' in query:
        send_email()

    elif 'thank u' in query or 'thank you' in query or 'thanks' in query:
        speak("Welcome Boss", "loving")
        
    elif 'exit' in query or 'escape' in query:
        try:
            speak("your command is fulfilled GoodBye Boss", "obedient")
            print("your command is fulfilled GoodBye Boss")
            sys.exit()
        except Exception as e:
            print(e)
            speak(f"sorry sir because of {e}\n", "confused")
            break
    elif 'search on google' in query or 'search' in query:
        speak("what should i search", "obedient")
        time.sleep(1)
        print("Speak.....")
        time.sleep(1)
        search = takeCommand()
        print(search)
        webbrowser.open(search)
    elif "joke" in query:
        joke = pyjokes.get_joke(language='en',category='neutral')
        speak(joke, "happy")
    '''elif ('iron man mod') in query:
        video = cv2.VideoCapture(0)
        mp_drawing = mp.solutions.drawing_utils
        mp_eyes = mp.solutions.hands
        #done=str("iron man mod")
        x = 2
        y = 3
        z = x+y
        for z in range(1,10):
            try:
                with mp_eyes.hands(min_detection_confidence= 0.7, min_tracking_confidence= 0.4) as eyes:
                    while video.isOpened():
                        _, frame = video.read()
                        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                        image = cv2.flip(image, 1)

                        imageHeight, imageWidth, _ = image.shape

                        results = eyes.process(image)


                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    if results.multi_hand_landmarks:
                        for num, hand in enumerate(results.multi_hand_landmarks):
                            mp_drawing.draw_landmarks(image, hand, mp_eyes.HAND_CONNECTIONS, 
                                                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                                    )

                    if results.multi_hand_landmarks != None:
                    for handLandmarks in results.multi_hand_landmarks:
                        for point in mp_eyes.HandLandmark:


                            normalizedLandmark = handLandmarks.landmark[point]
                            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)

                            point=str(point)

                            if point=='HandLandmark.INDEX_FINGER_TIP':
                                try:
                                    Eye_x=pixelCoordinatesLandmark[0]
                                    Eye_y=pixelCoordinatesLandmark[1]
                                    win32api.SetCursorPos((Eye_x*4,Eye_y*5))

                                except:
                                    pass
                cv2.imshow('Hand Tracking', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

                video.release()
            except:

                pass'''
    
    if any(x in query for x in ['bye', 'goodbye']):
        speak("your command is fulfilled GoodBye Boss", "obedient")
        print("your command is fulfilled GoodBye Boss")
        break
    elif "open gmail" in query:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now", "obedient")
        time.sleep(5)
    elif 'i love you' in query or 'i love u' in query:
        love()
    else:
        speak(f"Command '{query}' not set by master.")
    
# JarvisMain()
# # ===== Flask UI =====
# #app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# #@app.route("/logs")
# # def get_logs():
# #     logs = []
# #     while not log_queue.empty():
# #         logs.append(log_queue.get())
# #     return jsonify({"logs": logs})

# @app.route('/set_mode', methods=['POST'])
# def set_mode():
#     global mode
#     data = request.json
#     mode = data.get('mode', 'text')
#     print(f"Mode changed to: {mode}")
#     return jsonify({"status": "ok", "mode": mode})


# # @app.route("/send_command", methods=["POST"])
# # def send_command():
# #     data = request.get_json()
# #     cmd = data.get("cmd", "")
# #     log_queue.put({"type": "web_command", "text": cmd})
# #     return jsonify({"status": "ok"})

# @app.route('/send_text', methods=['POST'])
# def receive_text():
#     data = request.json
#     text = data.get('text')
#     command_queue.put({"type": "web_command", "text": text})
#     return jsonify({"status": "received", "text": text})

# # @app.route("/set_mode", methods=["POST"])
# # def set_mode():
# #     global mode
# #     data = request.get_json()
# #     mode = data.get("mode", "voice")
# #     add_chat("System", f"Mode set to {mode}")
# #     return jsonify({"status": "ok"})

# # def run_flask():
# #     app.run(debug=False, port=5000, use_reloader=False)

# # if __name__ == "__main__":
# #     flask_thread = threading.Thread(target=run_flask)
# #     flask_thread.start()
# #     JarvisMain()

# @socketio.on('start_listening')
# def handle_start_listening():
#     global listening
#     if not listening:
#         listening = True
#         print("Mic started listening (triggered from frontend)")
#         # Optionally start a new thread here to do your speech recognition and add_chat when done
#         def listen_thread():
#             global listening
#             # Your actual speech recognition logic can go here
#             # For demo, just simulate:
#             time.sleep(5)
#             spoken_text = "simulated speech input after mic start"
#             add_chat("You", spoken_text)
#             listening = False

#         threading.Thread(target=listen_thread).start()

# @socketio.on('stop_listening')
# def handle_stop_listening():
#     global listening
#     listening = False
#     print("Mic stopped listening (triggered from frontend)")


# if __name__ == '__main__':
#     socketio.run(app, debug=True)


'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = Main()
    gui.show()
    sys.exit(app.exec_())

'''

#while True():
 #   if "hi" in query or "hello" in query:
  #      speak("hello")
   # if "sorry" in query:
    #    speak("it's all right")
'''    
startExecution = (MainThread)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("label_8")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("label_6")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current.toString("hh:mm:ss")
        label_date = now.toString(Qt.ISODate)
        self.ui.time.setText(label_time)
        self.ui.Date.setText(label_date)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
#exit(app.exit_())
sys.exit(app.exec_())
'''






