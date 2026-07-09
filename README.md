# 🤖 Jarvis AI Assistant

A modular voice-controlled virtual assistant built with Python. Jarvis can understand voice commands, perform automation tasks, answer questions using Google's Gemini AI, and provide live weather updates.

## 🏗️ Project Architecture

                        +----------------+
                        |     User       |
                        | (Voice Input)  |
                        +-------+--------+
                                |
                                v
                        +----------------+
                        |   listen.py    |
                        | SpeechRecognition
                        +-------+--------+
                                |
                                v
                        +----------------+
                        |    main.py     |
                        | Wake Word Logic|
                        | Sleep/Wake Mode|
                        +-------+--------+
                                |
                                v
                        +----------------+
                        | commands.py    |
                        | Command Router |
                        +-------+--------+
                                |
        ---------------------------------------------------------
        |          |           |          |          |           |
        v          v           v          v          v           v
+--------------+ +---------+ +-----------+ +---------+ +---------+ +----------+
| actions.py   | | ai.py   | | weather.py| | speak.py| | Browser | | Apps     |
| Time & Date  | | Gemini  | |OpenWeather| | TTS     | | Search  | | Launcher |
+------+-------+ +----+----+ +-----+-----+ +----+----+ +---------+ +----------+
       |              |            |            |
       |              |            |            |
       +--------------+------------+------------+
                              |
                              v
                     +------------------+
                     |    User Output   |
                     | (Voice Response) |
                     +------------------+

## ✨ Features

- 🎤 Voice Recognition
- 🔊 Text-to-Speech
- 🤖 Gemini AI Integration
- 🌦️ Live Weather Information
- 🌐 Open Websites
- 🔍 Google Search
- 💻 Open Applications
- ⏰ Tell Time & Date
- 😴 Wake/Sleep Mode
- 🔐 Secure API Keys using `.env`

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- Google Gemini API
- OpenWeatherMap API
- Requests
- python-dotenv

## 📂 Project Structure

```
jarvis-ai-assistant/
│── main.py
│── listen.py
│── speak.py
│── commands.py
│── actions.py
│── ai.py
│── weather.py
│── requirements.txt
│── README.md
│── .gitignore
```

## 🚀 Installation

```bash
git clone https://github.com/itsnehabisht/jarvis-ai-assistant.git

cd jarvis-ai-assistant

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Run the assistant:

```bash
python main.py
```

## 🔮 Future Improvements

- Interrupt speech while speaking
- News Headlines
- Music Playback
- Volume Control
- Better Natural Language Understanding
- Reminder & Notes
- Smart Home Integration

## 👩‍💻 Author

**Neha Bisht**