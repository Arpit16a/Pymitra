# Pymitra - Voice Assistant

Pymitra is a Python-based voice assistant designed to simplify daily tasks through voice commands. It can open websites, play music, provide weather updates, tell jokes, share news, answer AI-based questions, and send WhatsApp messages.

## Features
- **Web Navigation**: Opens YouTube, LinkedIn, Google, and ChatGPT.
- **Music Playback**: Plays songs from a predefined music library via YouTube links.
- **Information Retrieval**: Provides current time, date, weather, jokes, and news.
- **AI-Powered Q&A**: Answers questions using the Mistral-7B model via DeepInfra API.
- **WhatsApp Messaging**: Sends messages to predefined contacts using WhatsApp Web.
- **Voice Interaction**: Supports wake word detection ("Pymitra", "Mitra", etc.) and command processing.

## Requirements
- Python 3.8+
- Libraries: Listed in `requirements.txt`
- APIs:
  - OpenWeatherMap (Weather)
  - NewsAPI (News)
  - DeepInfra (AI Q&A)
- A microphone for voice input

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pymitra.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pymitra
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Add your API keys to `.env`:
     ```bash
     WEATHER_API_KEY=your_openweathermap_key
     NEWS_API_KEY=your_newsapi_key
     DEEPINFRA_TOKEN=your_deepinfra_token
     ```
5. Set up contacts:
   - Copy `contacts_item_template.py` to `contacts_item.py`:
     ```bash
     cp contacts_item_template.py contacts_item.py
     ```
   - Edit `contacts_item.py` to add your contacts:
     ```python
     contacts = {
         "Name": "Phone Number"  # e.g., "John": "+1234567890"
     }
     ```
6. Create a `music_library.py` file:
   - Add your song names and YouTube links:
     ```python
     music = {
         "song name": "YouTube URL"  # e.g., "thunder": "https://www.youtube.com/watch?v=..."
     }
     ```

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Say the wake word ("Pymitra", "Mitra", etc.) to activate.
3. Issue commands like:
   - "Open YouTube"
   - "Play Shape of You"
   - "What's the weather in Mumbai?"
   - "Tell me a joke"
   - "Send WhatsApp to [Name] saying [Message]"
   - "AI, what's the capital of France?"
4. Say "close", "exit", or "goodbye" to stop the assistant.

## Project Structure
- `main.py`: Core script for wake word detection and command loop.
- `speech_engine.py`: Handles text-to-speech (pyttsx3, gTTS) and speech recognition.
- `command_handler.py`: Processes commands for web, music, info, and messaging.
- `music_library.py`: Contains a dictionary of song names and YouTube links.
- `contacts_item.py`: Stores contact names and phone numbers for WhatsApp messaging.
- `requirements.txt`: Lists all required Python libraries.
- `.gitignore`: Excludes sensitive and temporary files.
- `.env.example`: Template for environment variables.
- `contacts_item_template.py`: Template for contact details.

## APIs Used
- **OpenWeatherMap**: Weather data
- **NewsAPI**: News headlines
- **DeepInfra**: AI-powered question answering
- **Google Speech Recognition**: Speech-to-text conversion

## Limitations
- Requires an active internet connection.
- WhatsApp messaging relies on WhatsApp Web and may need manual intervention.
- Music library is limited to predefined songs.
- API keys and contacts must be configured manually.

## Contributing
Feel free to fork the repository, create a feature branch, and submit a pull request. Report issues or suggest features via GitHub Issues.

## License
This project is licensed under the MIT License.