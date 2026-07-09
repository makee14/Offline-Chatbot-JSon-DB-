----CHATBOT IS ALGORITHM----

loading all json file into a variable "data"

user will log in/sign in first... or it can enter guess mode but the information is limited

get user input

accessing all the keyword in "keywords", and per keyword turns it into a list
    the list should evaluate/compare one by one with the list of user input 
     means, before it will proceed to another dict of keywords, it should evaluate the first dict before the latter end

if the list of keyword from "keywords" is all in the list of word from the user input 
    get the length of the list and store it into variable also "keywordListLength"
    ex: keywordListLength = len(keywordList)
    
    Also, create a variable name "bestResponse," which initially has boolean value ("None"),
    . we will use None because the variable will have a list.
    We will store the "responses" from json if it is greater than the
    previous value of greatestLengthKeyword, which is initially 0
    ex: bestResponse = datas["responses"]
    
    The over all example of the code could be like:
    greatestLengthKeyword = 0
    bestResponse = None
    for datas in file:  # file is the chatbot_data
        for keyword in  datas["keywords"]:
            keywordList = keyword.split()
            for x in range(len(userInputList) - len(keywordList) + 1):
                if keywordList == userInputList[x:x + len(keywordList)]:
                    keywordListLength = len(keywordList)
                    if keywordListLength > greatestLengthKeyword:
                        bestResponse = datas["responses"]
    
    if bestResponse: # means if the bestResponse is true or has values in it
        return f"random.choice(bestResponse)"
    # if it does not found anything, we will store it into a separated json file.
        we could name it as "chatbotIsBaffled" 
    else:
        now = datetime.now()
        question = {
            "Question": userInput,
            "Date and Time Submitted": now.strftime(%m/%d/%y, %H: %M)
        }
        with open("chatbotIsBaffled.json", "w") as userIsNewQuestion:
            json.dump()
            
        return "I\'m very sorry. I cannot understand about that."
        
        # If bestResponse is TRUE or in other words it is not empty- we will store the context. 
            We will utilize regular expression
            The code will be develop soon  
                







def main():
    pass
    
if __name__ == "__main__":
    main()    
