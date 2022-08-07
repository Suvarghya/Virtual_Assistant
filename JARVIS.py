import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import pyjokes
import subprocess
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# It wishes me according to the time.
def wish_Me():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        talk('Good Morning sir ! How may I help you ?')
    
    elif hour>=12 and hour<18:
        talk('Good Afternoon sir ! How may I help you ?')

    else:
        talk('Good Evening sir ! How may I help you ?')

# Takes command through microphone and converts it into string.
def take_Command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        listener.pause_threshold = 1.1
        audio = listener.listen(source)
    try:
        print('Recognizing....')
        command = listener.recognize_google(audio , language='en-in')
        print(f"user said: {command}\n")
        
    except Exception as e:
        print('Any thing else sir? Please tell me...')
        talk('Any thing else sir? Please tell me.')
        return 'None'
    return command

if __name__ == "__main__":
    wish_Me()
    while True:
        command = take_Command().lower()
    # Playing any song:    
        if 'play music' in command:
            talk('which music you want to hear sir?')
            song = take_Command().lower()
            talk('Playing' + song)
            webbrowser.open('https://open.spotify.com/search/'+ song)
    # Play song on youtube: 
            #pywhatkit.playonyt('playing' + song)
    
    # Opening youtube:
        elif 'open youtube' in command:
            talk('opening youtube')
            webbrowser.open('https://www.youtube.com/')

    # To search something directly on youtube:
        elif 'play video' in command:
            talk('what do you want to see sir?')
            yt = take_Command().lower()
            pywhatkit.playonyt(yt)
    
    # Opening amazon:    
        elif 'open amazon' in command:
            talk('opening amazon')
            webbrowser.open('https://www.amazon.in/s?k=')
    
    # Opening flipkart:
        elif 'open flipkart' in command:
            talk('opening flipkart')
            webbrowser.open('https://www.flipkart.com/')
    
    # To oprn notepad:
        elif 'open notepad' in command:
            talk('opening notepad')
            path = "C:/Windows/system32/notepad.exe"
            notepad = subprocess.Popen(path)

        elif 'close notepad' in command:
            talk('closing notepad')
            notepad.terminate()

    # To shop any item from Flipkart
        elif 'shop' in command:
            buy = command.replace('shop','')
            talk(f"please tell me, from which website you want to buy {buy} ? flipkart or amazon ?")
            quary1 = take_Command().lower()
            if 'flipkart' in quary1:
                talk('showing results from flipkart')
                webbrowser.open('https://www.flipkart.com/search?q=' + buy )
            else:
                talk('showing results from amazon')
                webbrowser.open('https://www.amazon.in/s?k=' + buy )
    
    # Opening gmail:    
        elif 'open gmail' in command:
            talk('opening gmail')
            webbrowser.open('https://mail.google.com/')

    # Finding any loaction on google map:
        elif 'location' in command:
            locate = command.replace('location', '')
            webbrowser.open('https://www.google.co.in/maps/dir//' + locate)

    # To search any thing:
        elif 'search' in command:
            talk('sure sir ! please tell me what should I search ?')
            quary = take_Command().lower()
            webbrowser.open('https://www.google.com/search?q=' + quary)

    # To know about the current time:
        elif 'time'in command:
            time = datetime.datetime.now().strftime('%I:%M%p')
            print('current time is ' + time)
            talk('current time is ' + time)

    # To know about the current date:
        elif 'date'in command:
            date = datetime.datetime.now().strftime('%d-%m-%y')
            print('current date is ' + date)
            talk('current date is ' + date)

    # To know about SUSHI:
        elif 'who are you' in command:
            print("Hello ,I am Jarvis, the personal virtual assistent made by Suvarghya , I can look up answers for you , if you need anything just ask, your wish is my command")
            talk("Hello ,I am Jarvis, the personal virtual assistent made by Suvarghya , I can look up answers for you , if you need anything just ask, your wish is my command")

    # To know a about any one from wikipedia in shot:      
        elif 'tell me about' in command:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

    # To hear a joke:
        elif 'joke' in command:
            talk(pyjokes.get_joke())

    # Response of Thank you:
        elif 'thank you' in command:
            print("you're very welcome sir ! I'm honoured to serve")
            talk("you're very welcome sir ! I'm honoured to serve")
    
    # To stop Jarvis:
        elif 'quit' in command or 'no thanks'  in command:
            print("ok sir, just call me when you need")
            talk("ok sir, just call me when you need")
            exit()

    

        