import pyttsx3
assistant = pyttsx3.init()

def speak(text):
    assistant.say(text)
    assistant.runAndWait()


import speech_recognition as sr
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listining...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        
        except sr.UnknownValueError:
            print("assistant: Sorry, I could not understand the audio.")
            return ""
        
        except sr.RequestError as e:
            print(f"assistant: Could not request results; {e}")
            return ""


from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
user_input = listen()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("API_KEY"),
)
complition = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ]
)

answer = complition.choices[0].message.content

print(answer)
speak(answer)