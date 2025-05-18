import pyttsx3 as pyt
from gtts import gTTS
import pygame
import os
import tempfile
import speech_recognition as sr


# intializing the pyttsx3 engine as primary_engine, setting its properties

try :
    engine = pyt.init()
    engine.setProperty('voice', 0)
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 1)
    primary_engine_available = True
    dynamic_energy_threshold = True
except Exception as e:
    print(" pyttsx3 initialization failed:",e)
    primary_engine_available = False

def  speak(text):
    if not text:
        return
    
    try :
        if primary_engine_available:
            engine.say(text)
            engine.runAndWait()
        else:
              raise Exception("Primary engine not available")
        
    # If pyttsx3 fails, use gTTS as a fallback
      
    except Exception as e:
        print(" pyttsx3 failed, using gTTS:",e)
        try:
            tts = gTTS(text=text, Lang ='en')
            with tempfile.NamedTemporaryFile(delete = False, suffix=".mp3") as fp:
                temp_filename=fp.name
                tts.save(temp_filename)

            pygame.mixer.init()
            pygame.mixer.music.load(temp_filename)  
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue
            os.remove(temp_filename)
        except Exception as e:
            print ("Both the Engines failed",e) 

#wake word and listening using speech recognition

Wake_Word = ["pymitra","bhai mitra" ,  "mitra", "py mitra", "pi mitra"]   

recognizer = sr.Recognizer()
recognizer.enrgy_threshold = 200  # Lower means more sensitive
recognizer.pause_threshold = 0.5  # Controls silence length before command is sent


def listen_Wake_word():
    with sr.Microphone( ) as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source,timeout =10 , phrase_time_limit = 4)
            command = recognizer.recognize_google(audio).lower()
            # print("Heard:",command)
            if "close" in command:
                print(" Full shutdown triggered from wake word.")
                speak("Goodbye! Shutting down completely.")
                return "close"  #  special return to signal total shutdown
            # if Wake_Word in command:
            elif any(word in command for word in Wake_Word):
                print("Pymitra intiallizing")
                speak("Hello, I am Pymitra. Ram Ram!")
                return True
           

        except sr.WaitTimeoutError:
            return False
        except sr.UnknownValueError:
            return False
        except sr.RequestError as e:
            # print("🔌 API error:", e)
            return False    
        
# Function to listen for commands after the wake word is detecte

def listen_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)    
        print("Waiting for your command.....")
        try :
            audio = recognizer.listen(source,timeout=10, phrase_time_limit=6)
            print("Audio captured, recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("Your Command:",command)  
            return command   
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""
        except sr.WaitTimeoutError:
            speak("You didn't say anything.")
            return ""


