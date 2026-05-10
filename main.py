
import datetime
import time

name = input("Welcome!, Enter your name:")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning",name)
elif 11<= presentHour <=17:
    print("Good afternoon",name)
elif 17 <= presentHour <=20:
    print("Good evening",name)
else:
    print("Good night",name)


print("Namaste! Welcome to Your chatbot")
print("You can ask me basic question, Type 'bye' to exit from thr bot")

#Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "hello": "Hi, welcome. How can I help you",
    "how are you": "I am very fine. Thankyou so much",
    "who are you": "I am smart AI Chatbox Assitance",
    "motivate me": "Keep going. Every bug of your project makes you better developer.",
    "happy": "Great to hear that",
    "functions kya hote h" : "jaa kr youtube pr search kro chapter 7 saumya didi ka",
    "what is python" : "It is a programming language ",
    "namaskar" : "Hi, welcome. How can I help you",
    "Thankyou" : "Thankyou for using my system.Byeee!!"

}

def getResponseOfBot(userResponse):
    userResponse.lower()
    for eachkey in responses:
        if(eachkey in userResponse):
            return responses[eachkey]
    
    return "I am able to answer of this question yet.I will definitely learn soon"

while True:
    userInput = input("Please enter your message:")
    print("User:",userInput)
    time.sleep(1)
    reply = getResponseOfBot(userInput)
    print("Bot:",reply)

    if "bye" in userInput.lower():
        break
