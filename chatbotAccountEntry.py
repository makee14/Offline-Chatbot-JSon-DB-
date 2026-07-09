import json
import string as s
from chatbotHeader import *
import time as t
from chatbotFunctions import *

try:
    with open("userInfo.json", "r") as studentData:
        entry = json.load(studentData)
except:
    raise ValueError("Cannot found file: userInfo.json")
   
   
bold = "\033[1m"   
reset = "\033[0m" 
red = "\033[91m"
 
def logInUsingId():
    logInUsingIdHeader()
    idNum = input(bold + "Identification number: " + reset).strip()
    attempt = 5
    foundIdNum = False
    while True:
        userPass = input(bold + "Password: " + reset).strip()
                
        for student in entry:
            if student["idNum"] == idNum:
                foundIdNum = True
                if student["Password"] == userPass:
                    fName = student["fName"]
                    print("\nYou have successfully log in.")
                    print("-----------------------------\n")
                    print(bold + "Please wait..." + reset)
                    t.sleep(2)
                    return fName
                else:
                    clear()
                    attempt -= 1
                    logInUsingIdHeader()
                    print("Wrong combination of password!")
                    print(f"You have {attempt} attempt/s left.\n")
                    print(f"Identification number: {idNum}")
        if foundIdNum == False:         
            print(f"\nThere is no account using id number: {idNum}. Try to sign in first. ") 
            i = 5
            while i > 0:
                print(f"Redirecting you to the main page: {i}", end="\r")
                t.sleep(1)
                i -= 1
            break
        if attempt == 0:
            print("\nTry again later.")
            i = 5
            while i > 0:
                print(f"Redirecting you to the main page: {i}", end="\r")
                t.sleep(1)
                i -= 1
            break         
                     
def logInUsingEmail():
    logInUsingEmailHeader()
    email = input(bold + "Email account: " + reset).strip()
    foundEmail = False
    attempt = 5
    while True:
        userPass = input(bold + "Password: " + reset).strip()
    
        for student in entry:
            if student["email"] == email:
                foundEmail = True
                if student["Password"] == userPass:
                    fName = student["fName"]
                    print("\nYou have successfully log in.")
                    print("-----------------------------\n")
                    print(bold + "Please wait..." + reset)
                    t.sleep(2)
                    return fName
                else:
                    clear()
                    attempt -= 1
                    logInUsingEmailHeader()
                    print("Wrong combination of password!")
                    print(f"You have {attempt} attemp/s left.\n")
                    print(f"Email account: {email}")       
        if attempt == 0:
            print("\nTry again later.")
            i = 5
            while i > 0:
                print(f"Redirecting you to the main page: {i}", end="\r")
                t.sleep(1)
                i -= 1
            break   
        if foundEmail == False:  
            print(f"\nThere is no account using: {email}. Try to sign in first. ")  
            i = 5
            while i > 0:
                print(f"Redirecting you to the main page: {i}", end="\r")
                t.sleep(1)
                i -= 1
            break                                                
def signIn():
    signInHeader()
    print("\n>>>>>>>>>>>>>Enter your full name<<<<<<<<<<<<<<<<<")
    while True:
        fName = input("First: ").strip().capitalize()
        if len(fName) < 2:
            print("First name must be at least 2 characters long.")
        elif fName:
            break
        else:
            print("First name cannot be empty")

    while True:
        mName = input("Middle: ").strip().capitalize()
        if len(mName) < 2:
            print("Middle name must be at least 2 characters long.")
        elif mName:
            break
        else:
            print("Middle name cannot be empty.")
        
    while True:
        lName = input("Last: ").strip().capitalize()    
        if len(lName) < 2:
            print("Last name must be at least 2 characters long.")
        elif lName:
            break
        else:
            print("Last name cannot be empty.")

    print("\n----------------------------")
    while True:
        idNum = input("Identfication number: ").strip()
        if len(idNum) >= 17 and any(char.isdigit() for char in idNum):
            break
        else:
            print("WARNING: Please enter a valid id number.")

    print("")
    while True:
        email = input("Email: ").strip()
        if email.endswith("@gmail.com") or email.endswith("@phinmaed.com"):
            break
        else:
            print("WARNING: Please enter a valid email address.")

    for user in entry:
        if user["idNum"] == idNum or user["email"] == email:
            print("\nYou seems already signed in. Go to log in area\n")
            print("------------------------------------------------\n")
            print("Please wait. Redirecting you there...")  
            t.sleep(4)
            return None
    print("\n----------------------------")     
    while True:                 
        password = input("Password: ").strip()
        if len(password) < 8:
            print("Password should be consist of at least 8 characters.\n")
        elif password.isalpha():
            print("Password should contain a number.\n")
        elif password.isnumeric():
            print("Password should contain a letter.\n")
        else:
            break
        
    attempt = 5
    isSuccess = False
    while True:
        retryPass = input("Confirm password: ").strip()
        if attempt == 0:
            print("\nTry again later.\n")
            break
                    
        if password != retryPass:
            clear()
            attempt -= 1
            signInHeader()
            print("\nIncorrect password!")
            print(f"Name: {fName} {mName} {lName}\nEmail: {email}\nIdentification number: {idNum} \nPassword: {password}")
            continue
            
        else:
            isSuccess = True
            print("\nYou have successfully signed in. Go to log in area.")
            print("\n---------------------------------------------------\n\nPlease wait. Redirecting you there...")
            t.sleep(4)
            isSuccess = True
            break
    if isSuccess == True:
        newEntry = {
            "fName": fName,
            "mName": mName,
            "lName": lName,
            "idNum": idNum,
            "email": email,
            "Password": password
        }
        entry.append(newEntry)
         
        with open("userInfo.json", "w") as studentData:
            json.dump(entry, studentData, indent = 4)
            
def userAccountEntry():
    frontHeader()
    
    bold = "\033[1m"
    red  = "\033[91m"
    reset = "\033[0m"
    while True: 
        try:
            userResponse =int(input(bold + red + "You: " + reset))
            break
        except ValueError:
            clear()
            frontHeader()
            print("\nInvalid Response! Make sure to choose number from above. \n")
            
        
    if userResponse == 1:
        clear()
        return logInUsingId()
    elif userResponse == 2:
        clear()
        return logInUsingEmail()
    elif userResponse == 3:
        clear()
        signIn() 
        clear() 
        name = userAccountEntry()  
        return name     
    elif userResponse == 4:
        name = "Guess"
        return name
    
        
