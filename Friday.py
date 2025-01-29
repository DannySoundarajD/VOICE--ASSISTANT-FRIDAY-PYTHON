import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.setProperty('rate', 190)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            
            try:
                command = listener.recognize_google(voice).lower()
                print(f"Voice command: {command}")
                
                if "friday" in command:
                    command = command.replace('friday', '').strip()
                    return command
                else:
                    return command
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio.")
                talk("Sorry, I didn't catch that. Could you repeat?")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                talk("Sorry, there seems to be an issue with the speech recognition service.")
                return ""
            except Exception as e:
                print(f"Error during recognition: {e}")
                talk("Sorry, there was an error processing your command.")
                return ""
    
    except Exception as e:
        print(f"Error with microphone: {e}")
        talk("Sorry, I couldn't access the microphone. Please check your microphone and try again.")
        return ""


def run_friday():
    command = take_command()
    if not command:
        return True 

    try:
        
        if 'time' in command:
            times = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"boss, the current time is {times}.")

        elif "what is the meaning of your name" in command:
            talk("boss, my name stands for Female Replacement Intelligent Digital Assistant Youth.")

        elif "who gave you this name" in command:
            talk("boss, it's obviously you who gave me the name. And I am so glad to work with you, boss.")

        elif "are you single" in command:
            talk("Sorry, boss. I am not interested as I am committed to my work.")

        elif "joke" in command:
            talk(pyjokes.get_joke())

        
        elif "thank" in command:
            talk("It's my pleasure to help you, boss.")
        
        elif "are you there" in command:
            talk("Yes, boss. I am here. What can I do for you?")

        elif "who am i talking to" in command:
            talk("boss, you are talking to your virtual assistant named friday, created by you and inspired by Mr. Stark.")

        elif "what is your purpose" in command:
            talk("boss, my purpose is to help you in your daily work.")
            
            
        
        else:
            talk("Sorry, boss. I can't understand. Can you please say it again?")
    except Exception as e:
        print(f"Error in run_friday function: {e}")
        talk("Sorry, boss. I encountered an unexpected error while trying to process your request.")
    
    return True


while True:
    if not run_friday():
        break
