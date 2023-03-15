# Import necessary libraries
import openai
import pyttsx3
import speech_recognition as sr

# Set OpenAI API key
openai.api_key = "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"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to transcribe audio file to text using Google Speech Recognition API
def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    # Open the audio file using a context manager
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        # Use Google Speech Recognition API to transcribe the audio to text
        return recognizer.recognize_google(audio)
    except:
        # If an error occurs, print a message and return None
        print("Unknown error. Skipping transcription.")
        return None

# Function to generate a response to a given prompt using OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 3000,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    # Extract the generated text from the API response
    return response["choices"][0]["text"]

# Function to speak a given text using text-to-speech engine
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main program loop
def main():
    while True:
        print("Say 'Tell Me' and then ask the question...")
        # Use microphone input to listen for user input
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                # Use Google Speech Recognition API to transcribe user input
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "tell me":
                    # If the user says "tell me", prompt them to ask a question and listen for their input
                    filename = "input.wav"
                    print("Ask your question now...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        # Set the maximum recording time to infinity so the user can take as long as they need to ask the question
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            # Write the audio data to a file
                            f.write(audio.get_wav_data())
                    # Transcribe the audio file to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        # Print the transcribed text and generate a response using OpenAI API
                        print(f"You said: {text}")
                        response = generate_response(text)
                        print(f"Hype says: {response}")
                        # Speak the response using text-to-speech engine
                        speak_text(response)
            except Exception as e:
                # If an error occurs, print the error message
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
