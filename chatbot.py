import os
import pyttsx3
import speech_recognition as sr
import google.generativeai as gemini

# Set Gemini API key
gemini_api_key = 'geminikey'

# Initialize Gemini model
gemini.configure(api_key=gemini_api_key)
model = gemini.GenerativeModel('gemini-1.5-flash')

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to transcribe audio to text using Google Speech Recognition API
def transcribe_audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        print("Listening for your question...")
        try:
            audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

# Function to generate a response to a given prompt using Gemini API
def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error in generating response: {e}")
        return "I'm sorry, I couldn't process your request."

# Function to speak a given text using text-to-speech engine
def speak_text(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speaking the text: {e}")

# Main program loop
def main():
    while True:
        print("Ask your question...")
        text = transcribe_audio_to_text()
        if text:
            print(f"You said: {text}")
            response = generate_response(text)
            print(f"Assistant says: {response}")
            speak_text(response)
        else:
            print("Sorry, I could not understand your question. Please try again.")

if __name__ == "__main__":
    main()
