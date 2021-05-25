import speech_recognition as sr     #for converting audio to text
from win32com.client import constants, Dispatch #for converting text to audio
import datetime, wikipedia, webbrowser  #for date, time, web browser usage
name="Jarvis"      #default name of your assistant
def asst_speaks(audio):     #function for your assitant voice output
    print(name+": "+audio.upper())  #printing assitant voice in terminal
    speaker = Dispatch("SAPI.SpVoice")
    speaker.speak(audio)    #assistant speaks the relevant audio message
    del speaker
def greet():    #function for your assistant to greet you as per system time
    h = int(datetime.datetime.now().hour)   #taking the hour in a variable from system clock
    if h>=0 and h<12:
        asst_speaks("Good morning!")    #printing message as per hour range
    elif h==12:
        asst_speaks("Good noon!")       #printing message as per hour range
    elif h>12 and h<18:
        asst_speaks("good afternoon!")  #printing message as per hour range
    else:
        asst_speaks("good evening")     #printing message as per hour range
    asst_speaks("I am "+name+", how can I help you?")
def user_speaks():  #function to give user input to your assistant
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)   #setting listening time limit for the user here 5 secs
    try:
        print("Recognising...")
        com=r.recognize_google(audio,language="en-in")  #using google api to recognise sound
        print("You:"+com.upper())
    except :    #if poor audio quality or excessive background noise 
        asst_speaks("I didn't get you. Try saying it again!")
    return com
def reg_browser():  #Register Chrome as the browser to be used here
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('google-chrome', None,webbrowser.BackgroundBrowser(chrome_path))
def main():     #driver code
    reg_browser()
    greet()
    while(True): #infinite loop for seamless interaction
        com=user_speaks().lower()   #taking user command
        if "wikipedia" in com: #if users says to wiki something
            asst_speaks("Searching wikipedia")
            com=com.replace("wikipedia","")
            res=wikipedia.summary(com,sentences=2)  #extracting summary of the wikipedia search
            asst_speaks("According to wikipedia:"+res)  #audio output of the summary
            asst_speaks("Want to know more! Shall I open wikipedia?")
            dec=user_speaks().lower()
            if "yes" or "yeah" in dec:
                webbrowser.get("google-chrome").open("en.wikipedia.com")    #opens wikipedia home page
            else:
                asst_speaks("As you wish sir!")
        elif "open youtube" in com: #if users says to open youtube
            webbrowser.get("google-chrome").open("youtube.com")
        elif "open google" in com:  #if user says to open google
            webbrowser.get("google-chrome").open("google.com")
        elif "open stackoverflow" in com:   #if user says to open stack overflow
            webbrowser.get("google-chrome").open("stackoverflow.com")
        elif "open geeks for geeks" in com: #if user says to open Geeeks for Geeks
            webbrowser.get("google-chrome").open("geeksforgeeks.com")
        elif "open codechef" in com:    #if user says to open Codechef
            webbrowser.get("google-chrome").open("codechef.com")
        elif "open github" in com:  #if user says to open Github
            webbrowser.get("google-chrome").open("github.com")
        elif "play music" in com or "open spotify" in com:  #if user says to open Spotify
            webbrowser.get("google-chrome").open("spotify.com")
        elif "open hotstar" in com: #if user says to open Hotstar
            webbrowser.get("google-chrome").open("hotstar.com")
        elif "time" in com: #if user asks the time
            timestr=datetime.datetime.now().strftime("%H:%M")
            asst_speaks("Sir the time is "+timestr)
        elif "your name" in com:    #if user asks the assistant his name
            asst_speaks("Hi, my name is"+name)
        elif "about creator" in com:    #if user wants to know about the creator
            asst_speaks("I am one of the many creations of sir Dipak Ghosh. Want to know more?")
            dec=user_speaks().lower()
            if "yes" or "yeah" in dec:
                webbrowser.get("google-chrome").open("https://dgreat49251.github.io/dipak.ghosh/")  #more about the creator
            else:
                asst_speaks("As you wish sir!")
        elif "exit" or "shutdown" in com:   #if user says to exit
            asst_speaks("Are you sure you want to exit?")
            dec=user_speaks().lower()
            if "yes" or "yeah" in dec:  #confirmation
               break
            else:
                continue
        else:
            continue
main()  #executing the driver code