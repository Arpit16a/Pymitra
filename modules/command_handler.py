import datetime
import webbrowser
from modules.speech_engine import speak
import modules.music_library as music_library
import requests
import pywhatkit
import pyautogui
import datetime
import time
import modules.contacts_item as contacts_item

WEATHER_API_KEY = "you_API_key"
# Replace with your actual OpenWeatherMap API key
NEWS_API_KEY = "you_API_key" 
# Replace with your actual OpenWeatherMap API key

def get_weather(city="Delhi"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return f"Sorry, I couldn't find weather data for {city}."
        
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"The weather in {city} is {weather_desc} with a temperature of {temp}°C and humidity of {humidity}%."
    except Exception as e:
        return "Sorry, I am unable to get the weather right now."

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        joke = response.json()
        setup = joke.get("setup")
        punchline = joke.get("punchline")
        return f"Here's a joke for you: {setup} ... {punchline}"
    except Exception as e:
        return "Sorry, I couldn't fetch a joke right now."

def get_news():
    try:
        url = f"https://newsapi.org/v2/everything?q=india&apiKey={NEWS_API_KEY}&pageSize=3"
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get("articles", [])
        if not articles:
            return "Sorry, no news available at the moment."
        
        news_brief = "Here are the top news headlines: "
        for i, article in enumerate(articles):
            news_brief += f"\n{i+1}. {article['title']}"
        return news_brief
    except Exception as e:
        return "Sorry, I couldn't fetch news right now."

def send_whatsaap_message(name,phone_number, message):
    try:
        current_time= datetime.datetime.now()
        send_time_hour = current_time.hour
        send_time_minute = current_time.minute + 2

        speak(f"sending message to {name}")
        print(f"To:{name} \n Message:{message}")

        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)
        
        speak("Message scheduled. Please wait, it will open WhatsApp Web")
        print("Waiting to send...")

        time.sleep(15)
        pyautogui.hotkey('ctrl', 'w')  # Close browser tab
    
    except Exception as e:
        print("Error sending WhatsApp message:", e)
        speak("Something went wrong while sending the WhatsApp message.")   
    return True


def handle_command(command):
    command = command.lower()
    current_time = datetime.datetime.now().strftime("%H:%M")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    """
    Handle the command given by the user.
    """
    if "linkedin" in command:
        speak("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com/in/arpit-pandey-ap09/")
        return True
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True
    
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True

    elif "chatgpt" in command or "chat gpt" in command or "chat" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com/")
        return True
    
    elif "play" in command:
        # Extract song name after 'play'
        song_name = command.replace("play", "").strip()  # e.g. "thunder", "shape of you"
        
        # Check if the song is in the music dictionary
        if song_name in music_library.music:
            link = music_library.music[song_name]
            speak(f"Playing {song_name}")
            webbrowser.open(link)
            return True
        
        else:
            speak(f"Sorry, I don't have the song {song_name} in the library.")
            return True
    
    elif "weather" in command:
        # Extract city if provided: e.g. "weather in Mumbai"
        city = "Delhi"  # default city
        if "in" in command:
            parts = command.split("in")
            city = parts[-1].strip()
        weather_report = get_weather(city)
        speak(weather_report)
        return True

    elif "joke" in command:
        joke = get_joke()
        speak(joke)
        return True

    elif "news" in command:
        news = get_news()
        speak(news)
        return True
    
    elif "what is the time" in command:
        
        speak(f"The time is {current_time}")
        print(f"The time is {current_time}")
        return True
    
    elif "what is the date " in command:
        
        speak(f"Today's date is {current_date}")
        print(f"Today's date is {current_date}")
        return True
    
    elif any(phrase in command for phrase in ["who are you", "hu r u", "who r u", "who you are"]):

        speak("I am Pymitra, your personal assistant.")
        return True

    elif  any(greet in command.lower() for greet in ["hi", "hello", "hey", "heya"]):  
        speak("Hello!It' Pymitra here , How can I assist you today?")
        return True
    
    elif "exit" in command or "goodbye" in command or "stop" in command:
        speak("Goodbye! Going to sleep.")
        return False  # signal to break loop
    
    elif "ai" in command:
        prompt = command.replace("ai","").strip()
        if not prompt:
            speak("what would you like to ask?")
            return True
        
        try:

            headers= {
                "Authorization":"Bearer xBJxHu8TKR4bxPiMkHDJuSwhRyiDCsOc",
                "Content-Type":"application/json"
            }

            data = {
                "model" :"mistralai/Mistral-7B-Instruct-v0.1",
                "messages": [
                    {"role": "user","content" :prompt}]
            }
            
            response = requests.post("https://api.deepinfra.com/v1/openai/chat/completions",headers=headers,json=data)

            if response.status_code == 200:
                response_data = response.json()["choices"][0]["message"]["content"]
                print(response_data)
                speak(response_data)
            else:
                print("Error:", response.status_code, response.text)
                speak("Sorry, I couldn't process your request.")

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I couldn't process your request.")
        return True    

    elif "whatsapp" in command and "saying" in command:
        try:
            # Normalize command
            cmd = command.lower()

            # Look for contact name match
            matched_name = None
            for name, phone_number in contacts_item.contacts.items():
                if name.lower() in cmd:
                    matched_name = name
                    break

            if not matched_name:
                speak("I couldn't find the contact you're trying to message.")
                return True

            # Extract message after 'saying'
            if "saying" not in cmd:
                speak("Please say your message with the word 'saying'")
                return True

            message = cmd.split("saying", 1)[-1].strip()

            if not message:
                speak("Please say your message after 'saying'.")
                return True

            phone_number = contacts_item.contacts[matched_name]
            speak(f"Scheduling message to {matched_name} on WhatsApp")

            if "instant" in cmd:
                pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=False)
            else:
                now = datetime.datetime.now()
                pywhatkit.sendwhatmsg(phone_number, message, now.hour, now.minute + 2)

            # speak("Message is ready to send. Please wait while WhatsApp Web opens.")
            time.sleep(15)
            pyautogui.hotkey('ctrl', 'w')
            return True

        except Exception as e:
            print("Error sending WhatsApp message:", e)
            speak("Something went wrong while trying to send the message.")
            return True

    else:
        speak("Sorry, I didn't understand that.")