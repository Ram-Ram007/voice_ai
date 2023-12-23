import speech_recognition as sr
from gtts import gTTS
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    # Using pyttsx3 for playback
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            response = "You said: " + user_input  # Your AI logic here
            print("AI:", response)
            speak(response)

if __name__ == "__main__":
    main()
