# Voice-Activated AI Assistant

This project implements a voice-activated AI assistant using Google's Gemini API for generating responses and Google Speech Recognition API for transcribing audio to text. The assistant listens to user queries, generates appropriate responses using the Gemini API, and speaks the responses using a text-to-speech engine.

## Features

- Voice input using the microphone
- Text transcription using Google Speech Recognition API
- AI-generated responses using Gemini API
- Voice output using pyttsx3 text-to-speech engine

## Requirements

- Python 3.6 or higher
- `pyttsx3` for text-to-speech
- `speech_recognition` for audio transcription
- `google-generativeai` for AI-generated responses

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Hype16/chatgptPre.git
    cd chatgptPre
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install pyttsx3 speechrecognition google-generativeai
    ```

## Setup

1. Obtain a Google Gemini API key and set it in the script.

2. Update the `gemini_api_key` variable in the script with your Gemini API key:
    ```python
    gemini_api_key = 'YOUR_GEMINI_API_KEY'
    ```

## Usage

Run the main script:
```sh
python main.py
