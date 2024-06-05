import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.setProperty('pitch', 1)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning Boss...")
    elif 12 <= hour < 17:
        speak("Good Afternoon Master...")
    else:
        speak("Good Evening Sir...")

def take_command(command):
    command = command.lower()

    if 'hey' in command or 'hello' in command:
        speak("Hello Sir, How May I Help You?")
    elif 'open google' in command:
        webbrowser.open("https://google.com")
        speak("Opening Google...")
    elif 'open youtube' in command:
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube...")
    elif 'open facebook' in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook...")
    elif 'what is' in command or 'who is' in command or 'what are' in command:
        webbrowser.open(f"https://www.google.com/search?q={command.replace(' ', '+')}")
        speak(f"This is what I found on the internet regarding {command}")
    elif 'wikipedia' in command:
        webbrowser.open(f"https://en.wikipedia.org/wiki/{command.replace('wikipedia', '').strip()}")
        speak(f"This is what I found on Wikipedia regarding {command}")
    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time}")
    elif 'date' in command:
        date = datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {date}")
    elif 'calculator' in command:
        # Note: Opening calculator varies by OS; this is for Windows
        speak("Opening Calculator")
        os.system('calc')
    else:
        webbrowser.open(f"https://www.google.com/search?q={command.replace(' ', '+')}")
        speak(f"I found some information for {command} on Google")

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speak("Initializing NOVA...")
    wish_me()

    while True:
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            take_command(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("Sorry, I am having trouble connecting to the service.")

if __name__ == "__main__":
    main()
