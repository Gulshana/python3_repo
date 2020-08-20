import pyttsx3
import os

pyttsx3.speak("Welcome to my tools. Which program you want me to launch for you from the list below.")
print()
print("           ------- Chrome Browser -------")
pyttsx3.speak("Chrome Browser")
print("           ----------- Notepad ----------")
pyttsx3.speak("Notepad")
print("           ---- Windows Media Player ----")
pyttsx3.speak("Windows Media Player")
print()
print(" Type \"Done\" or \"Bye\" if you wish to exit My tools.")
pyttsx3.speak(" Type \"Done\" or \"Bye\" if you wish to exit My tools.")
print()
while True:
    print("You can type here : ",end='')
    p  = input()
    if ("not " in p or "dont" in p or "don\'t" in p):
        print("Ok, let me know if you want to launch something form the list above something else you want me to launch.")
        pyttsx3.speak("Ok, let me know if you want to launch something form the list above something else you want me to launch.")
    else:
        if ("launch" in p or "open" in p or "run" in p or "start" in p):
            if ("chrome" in p or "browser" in p or "chrome browser" in p):
                pyttsx3.speak("Suer, opening Chrome Browser for you.")
                pyttsx3.speak("Close Chrome Browser once you are done and wish to lauch another program from the list.")
                pyttsx3.speak(" Type \"Done\" or \"Bye\" if you wish to exit My tools.")
                os.system("chrome")
            elif("textpad" in p or "notepad" in p):
                pyttsx3.speak("Ok, Opening notepad for you")
                pyttsx3.speak("Close Notepad once you are done and wish to lauch another program from the list.")
                pyttsx3.speak(" Type \"Done\" or \"Bye\" if you wish to exit My tools.")
                os.system("notepad")
            elif("media player" in p or "player" in p or "media" in p or "windows media player" in p):
                pyttsx3.speak("Nice choice, starting Windows media player for you.")
                pyttsx3.speak("Close Windows Media Player once you are done and wish to lauch another program from the list.")
                pyttsx3.speak(" Type \"Done\" or \"Bye\" if you wish to exit My tools.")
                os.system("wmplayer")
            else:
                print("I can only launch the programs from above list. Soon we will add more programs.")
                pyttsx3.speak("I can only launch the programs from above list. Soon we will add more programs.")
        elif("done" in p or "bye" in p):
            pyttsx3.speak("Good Bye.... Have a good day.")
            break
        else:
            print("Please select a program from above list to launch.")
            pyttsx3.speak("Please select a program from above list to launch.")

