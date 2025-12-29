# 🧞‍♂️ JARVIS AI Assistant (Persian Edition)

> An intelligent, voice-activated desktop assistant built with Python, capable of controlling the OS, chatting naturally in Persian, and managing daily tasks.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-green?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange?style=for-the-badge)

## 📸 Demo

![App Screenshot](screenshot.png)
*(Place your screenshot here)*

## 📖 Overview

This project is not just a simple chatbot; it's a **System Commander**. It uses **Picovoice Porcupine** for offline wake-word detection ("Jarvis") and integrates **Google's Gemini AI** to provide witty, context-aware responses in Persian.
The application features a modern, dark-themed GUI built with **CustomTkinter** and supports multi-threaded operations to ensure a lag-free experience.

## ✨ Key Features

- **🗣️ Natural Persian Interaction:** Speaks and understands Persian with a high-quality neural voice (Edge-TTS).
- **👂 Smart Wake-Word Detection:**
  - **Voice Mode:** Say "Jarvis" -> It replies "Janom?" (Yes dear?).
  - **Manual Mode:** Click the Mic button -> Hear a system beep (Fast mode).
- **🧠 Generative AI Brain:** Powered by **Google Gemini 1.5 Flash** for smart, witty, and concise conversations.
- **💻 OS Automation:**
  - Control System Volume.
  - Take Screenshots.
  - Check Battery & CPU stats.
  - Minimize Windows / Show Desktop.
- **🎵 Media Control:** Plays music/videos directly on YouTube via voice commands.
- **⛅ Real-time Info:** Fetches live Weather, Time, and Date.
- **🎨 Modern UI:** Clean, Dark-themed interface with animated status indicators.

## 🛠️ Tech Stack

- **Core:** Python 3.11
- **GUI:** CustomTkinter (Modern Tkinter wrapper)
- **Wake Word:** Picovoice Porcupine (Offline)
- **Speech-to-Text:** Google Speech Recognition
- **Text-to-Speech:** Microsoft Edge TTS (Online Neural voice)
- **LLM:** Google Generative AI (Gemini)
- **Automation:** PyAutoGUI, Psutil, PyWhatKit

## 🚀 Installation & Setup

1. **Clone the repository:**
   git clone https://github.com/YOUR_USERNAME/Jarvis-AI-Assistant.git
   cd Jarvis-AI-Assistant
   
2. Install dependencies:
pip install -r requirements.txt

3. Configure API Keys:
Get a free AccessKey from Picovoice Console.
Get a free API Key from Google AI Studio.
Open wakeword.py and paste your Picovoice Key.
Open brain.py and paste your Google Gemini Key.

4. Run the App:
python gui_app.py

📦 Building EXE (Standalone)
To create a standalone executable file for Windows:
pyinstaller --noconfirm --onefile --windowed --name "JarvisPro" --collect-all customtkinter --collect-all pvporcupine --collect-all pvrecorder --collect-all speech_recognition --collect-all pywhatkit --hidden-import="pyaudio" --hidden-import="winsound" --icon="NONE" gui_app.py

🤝 Contribution
Feel free to fork this repository and submit pull requests. Any improvements, especially regarding new "Skills" for Jarvis, are welcome!

Developed with ❤️ by Mahdi Najjarian

