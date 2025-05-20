# # import speech_recognition as sr
# # import pyttsx3 as pyt
# # import webbrowser as wb

# # recognizer= sr.Recognizer()
# # engine = pyt.init()

# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()

# # if __name__ == "__main__":
# #     speak("Hello, I am your assistant")
# #     engine.setProperty('rate', 125)

# from modules.speech_engine import speak
    
# # speak("Hello! Your speech engine is working.")


# from modules.speech_engine import listen_Wake_word  # assuming your wake word code is in listener.py
# import time
# from modules.speech_engine import listen_command  # assuming your command listening code is in listener.py
# from modules.command_handler import handle_command  # assuming your command handling code is in listener.py

# # while True:
# #     print("Initializing...")
# #     activated = listen_Wake_word()
# #     if activated:
# #         print("Wake word detected. Listening for commands...")
        
    
# #     while True:

# #             command = listen_command()
# #             if command:    
# #                continue_listening= handle_command(command)
# #                if not continue_listening:
# #                      break
# #             else:
# #                 speak("Sorry, I didn't catch that.")
# #             # print("Pymitra intiallizing")
# #             # speak("Hello, I am Pymitra. Ram Ram!")
# #             # For now just wait 2 seconds then go back to listening again
# #             time.sleep(1)




# try:
#     while True:
#         print("Initializing...")
#         activated = listen_Wake_word()

#         if activated:
#             print("Wake word detected. Listening for commands...")
        

#             while True:
#                 command = listen_command()
#                 if command:
#                     continue_listening = handle_command(command)
#                     if not continue_listening:
#                         break
#                 else:
#                     speak("Sorry, I didn't catch that.")
#                 time.sleep(1)

# except KeyboardInterrupt:
#     print("\n[INFO] Pymitra stopped by user. Exiting gracefully.")
#     speak("Goodbye! See you soon.")






# from modules.speech_engine import speak, listen_Wake_word, listen_command
# from modules.command_handler import handle_command
# import time

# try:
#     while True:
#         print(" Waiting for wake word...")
#         activated = listen_Wake_word()

#         if activated:
#             print(" Activated! Ready to take commands...")

#             while True:
#                 command = listen_command()
#                 if command:
#                     if "close" in command:
#                         print(" Exiting completely.")
#                         speak("Goodbye! Going to sleep completely.")
#                         running = False
#                         break
#                     continue_listening = handle_command(command)
#                     # if not continue_listening:
#                     if "exit" in command or "goodbye" in command:
#                         print(" Exiting command loop.")
#                         break
#                 else:
#                     print("No valid command heard.")
                
#                 # Pause to avoid microphone race condition
#                 time.sleep(1)
                   

# except KeyboardInterrupt:
#     print("\n Pymitra stopped. Exiting gracefully.")
#     speak("Goodbye! See you soon.")



# from modules.speech_engine import speak, listen_Wake_word, listen_command
# from modules.command_handler import handle_command
# import time

# try:
#     running = True
#     while running:
#         print(" Waiting for wake word...")
#         activated = listen_Wake_word()

#         if activated:
#             print(" Activated! Ready to take commands...")
#             while True:
#                 command = listen_command()

#                 if command:
#                     # Check for "close" first, to end everything
#                     if "close" in command:
#                         print(" Exiting completely.")
#                         speak("Goodbye! Going to sleep completely.")
#                         raise SystemExit  # or use break_flag
#                         running = False
                        
#                     continue_listening = handle_command(command)

#                     if not continue_listening:  # handles 'exit' or 'goodbye'
#                         print(" Exiting command loop.")
#                         break
#                 else:
#                     print("No valid command heard.")

#                 # Pause to avoid microphone locking
#                 time.sleep(1)

# except KeyboardInterrupt:
#     print("\n Pymitra stopped. Exiting gracefully.")
#     speak("Goodbye! See you soon.")
# except SystemExit:
#     print("\n SystemExit received. Terminating Pymitra.")
#     speak("Goodbye! See you soon.")

from modules.speech_engine import speak, listen_Wake_word, listen_command
from modules.command_handler import handle_command
import time

try:
    running = True

    while running:
        print("Waiting for wake word...")
        wake_status = listen_Wake_word()

        #  Check if wake_status explicitly requested shutdown
        if wake_status == "close":
            print(" Shutting down from wake word.")
            speak("Goodbye! Going to sleep completely.")
            break

        #  If wake word heard (wake_status is True), go into command mode
        if wake_status is True:
            print(" Activated! Ready to take commands...")

            while True:
                command = listen_command()
                if command:
                    #  Allow full shutdown during command phase
                    if "close" in command:
                        print(" Full shutdown triggered from command phase.")
                        speak("Goodbye! Going to sleep completely.")
                        running = False
                        break

                    # Handle regular commands
                    continue_listening = handle_command(command)
                    if not continue_listening:
                        # print(" Exiting command loop.")
                        continue
                else:
                    print("No valid command heard.")
                    speak("Sorry, I didn't catch that. Can you repeat?")
                    continue  # Stay in command mode and keep listening
                time.sleep(1)
except KeyboardInterrupt:
    print("\ Pymitra stopped. Exiting gracefully.")
    speak("Goodbye! See you soon.")
