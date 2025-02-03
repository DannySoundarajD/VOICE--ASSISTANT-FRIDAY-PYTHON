import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import time
import keyboard

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
        if "play from youtube" in command:
            song = command.replace('play from youtube', '').strip()
            talk(f"Alright, boss. Playing the song '{song}' as you asked for.")
            pywhatkit.playonyt(song)
            return False

        elif 'time' in command:
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

        elif "search"  in command:
            search_query = command.replace("search", "").strip()
            talk(f"Searching for {search_query} on Google.")
            pywhatkit.search(search_query)
            return False
            
            
        elif "open spotify" in command:
            talk("Alright Boss")
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write('Spotify')
            time.sleep(1)
            pyautogui.press('enter')
            

        elif "play from spotify" in command:
            song = command.replace("play from spotify", "").strip()
            talk(f"Alright, boss. Playing the song '{song}' as you asked for from Spotify.")
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write('Spotify')
            time.sleep(1)
            pyautogui.press('enter')
            
            
            time.sleep(7)
            pyautogui.hotkey('ctrl', 'k')
            time.sleep(1)
            pyautogui.write(song, interval=0.3)
            time.sleep(1)
            keyboard.send("enter")
            time.sleep(2)
            talk(f"The {song} is playing boss")
            return False

        elif "close" in command:
            talk("Alright, boss. I am closing the application.")
            pyautogui.hotkey('alt', 'F4')
            return False


        elif "go to sleep" in command:
            talk("Alright, boss. Turning off my system. Goodbye!")
            return False  

        else:
            talk("Sorry, boss. I can't understand. Can you please say it again?")
    except Exception as e:
        print(f"Error in run_friday function: {e}")
        talk("Sorry, boss. I encountered an unexpected error while trying to process your request.")
    
    return True


while True:
    if not run_friday():
        break
