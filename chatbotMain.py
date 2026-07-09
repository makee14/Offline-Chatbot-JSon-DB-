import string as s
from chatbotFunctions import *
from chatbotAccountEntry import *
from chatbotHeader import *
from chatbotFunctions import *
import time as t
import textwrap
import sys
 
userBye = ["bye", "goodbye", "see you later"]
    #BAsic ASNI Codes
bold = "\033[1m"
red = "\033[91m"
green = "\033[92m"
cyan = "\033[96m"
reset = "\033[0m" #we need this so it stop from using to everything
diffSound = ["\a", "\07", "\007\007", "\033\a"]
    
def typeAnimate(text):
    for char in text:
        sys.stdout.write(cyan + char + random.choice(diffSound))
        sys.stdout.flush()
        t.sleep(0.010)
    print(reset)

def chat():
    #Takin user input
    userInput = input(bold + red + "You: " + reset).lower().replace(".", "")

    print(bold + green +  "Bot is thinking..." + reset, end="\r")
    t.sleep(.9)
    print("\r\033[K", end='') #This remove the current line, which above this code
    
    for bye in userBye:
        if userInput.startswith(bye):
            typeAnimate("Okayyy! See you next time!\n")
            i = 5
            while i > 0:
                print(bold + cyan + f"Redirecting you to the main page: {i}" + reset, end="\r")
                t.sleep(1)
                i -= 1
            clear()
            main()
    
    print(bold + green + f"Chatbot: " + reset, end="")
    botResponse = chatbot(userInput)
    wrapResponse = textwrap.fill(botResponse, width=100) 
    
    saveChat(userInput, botResponse)
    
    typeAnimate(wrapResponse)
    
    
    chat()
    
def main():
    #after sign in or log in,  it will return the first name
    name = userAccountEntry()
       
    while True:
        if not name:
            clear()
            main()  
        break
    if name: 
        if name == "Guess":
            clear()
            frontGuessHeader()
            chat()
        else:
            clear()
            frontHeaderNew(name)
            chat()
        
if __name__ == "__main__":
    main()
