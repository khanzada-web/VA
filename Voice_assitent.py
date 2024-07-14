import speech_recognition as sr
import pyttsx3
from playsound import playsound

recognizer = sr.Recognizer()
tts = pyttsx3.init()

def Speak(text):
    tts.say(text)
    tts.runAndWait()

def Listen():
    with sr.Microphone() as source: 
        print("Hello Sir I Am listening:-")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You Said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

def main():
    Speak("Hello! How can I help you today?")
    while True:
        command = Listen()
        if "exit" in command or "quit" in command:
            Speak("Goodbye!")
            break
        elif "how are you" in command:
            Speak("I am fine, thank you!")
        elif "your name" in command:
            Speak("I am your personal assistant.")
        elif "your name" in command:
            Speak("I am your personal assistant.")
        elif "bye" in command:
            Speak("Good Bye Sir Have A Nice Day")
            break
        elif "bored" in command:
            Speak("Can i Sing a Song for you ?")
        elif "sing" in command:
            playsound("D:\Cubex_interShip_projects\Music App\music\1.mp3")
        else:
            Speak("Sorry, I didn't Hear you Sir i know its my Fault. Please try again.")

if __name__ == "__main__":
    main()
