import pyttsx3

stop = "yes"
while 1:
    text = input("enter something here : ")
    if text == "no":
        engine = pyttsx3.init()
        engine.say("Thank you so much.I am very happy that you take help from me?")
        engine.runAndWait()
        engine.stop()        
        print("Thanks?")
        break
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()