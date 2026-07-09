import json
import random
import time
import string as s
from datetime import datetime
import string as s
from chatbotFunctions import *
import os

try:
    # Load chatbotData.json
    with open("chatbotData.json", "r") as file:
        data = json.load(file)
    with open("chatbotIsBaffled.json", "r") as inquiry:
        inquiries = json.load(inquiry)
    with open("chatbotChatHistory.json", "r") as chatHistory:
        chatHistories = json.load(chatHistory)
    
except:
    raise FileNotFoundError("Cannot found the json file")

userGreeting = ["hi", "hello", "hey"]
botGreeting = ["Hello! ", "I'm glad to hear from you. "]
apology = ["Sorry, I cannot understand. Would you mine elaborate it?", 
"I'm sorry. It seems that is out of my knowledge.",
"Opsss... I'm sorry, I don't know about that."]
  
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def saveChat(user, bot):
    now = datetime.now()
    newChat = {
        "Date and Time Submitted" : now.strftime("%m/%d/%y, %H: %M"),
        "User": user,
        "Bot" : bot
        }
    chatHistories.append(newChat)
    with open("chatbotChatHistory.json", "w") as savedChat:
        json.dump(chatHistories, savedChat, indent=4) 
        
def chatbot(userInput):
    
    inputList = userInput.strip(s.punctuation + s.whitespace).split()
    
    bestMatch = None #this if both the list and inputList is same
    bestMatchLen = 0 
    bestPossibleResponse = {} #this if not same but it got some keywords
    bestPossibleResponseLen = 0 
 
    
    if len(inputList) <= 3 and any(word.startswith(greeting) for word in inputList for greeting in userGreeting):
        return random.choice(botGreeting)
        
    for info in data:
        for key in info["keywords"]: 
            keywordList = key.split()
            if len(keywordList) == 1:
                for y in range(len(inputList)):#this if the keyword is only one
                    if keywordList == inputList[y]:
                        return random.choice(info["responses"])
            for x in range(len(inputList) - len(keywordList) + 1): #keyword must be greater than 1
                if keywordList == inputList[x:x + len(keywordList)]:
                    keywordListLen = len(keywordList)
                    if keywordListLen > bestMatchLen:
                        bestMatchLen = keywordListLen
                        bestMatch = info
                    elif keywordListLen == bestMatchLen and bestMatchLen > 0:
                        bestPossibleResponseLen
                        bestPossibleResponse.update(info)
                    elif keywordListLen > bestPossibleResponseLen: #this is when kwLen < bmLen and kwLen > bprLen
                        bestPossibleResponse.clear() #remove all items in the dict
                        bestPossibleResponse.update(info)


    if bestMatch:
        return random.choice(bestMatch["responses"]) 
    elif bestMatch == None and bestPossibleResponse:
        return random.choice(bestPossibleResponse["responses"])
    else:
        now = datetime.now()
        newInquiry = {
            "Date and Time Submitted" : now.strftime("%m/%d/%y, %H: %M"),
            "Question: ": userInput.capitalize()}
        inquiries.append(newInquiry)
        with open("chatbotIsBaffled.json", "w") as wInquiries:
            json.dump(inquiries, wInquiries, indent=4)
        return random.choice(apology)
                

   

def frontPage():
    print("""
  ----------------------------------
|| Hello! Welcome to PUCU's Chatbot ||
  ----------------------------------
  [1] LOG-IN USING ID NUMBER
  [2] LOG-IN USING EMAIL
  [3] SIGN-IN A NEW ACCOUNT
  [4] GUESS
  
""")
    
  
