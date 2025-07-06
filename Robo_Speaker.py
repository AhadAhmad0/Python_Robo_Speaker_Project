import pyttsx3

engine = pyttsx3.init()
print("Welcome to Robo Speaker (Created by Ahad)")

while True:
    speak = input("Enter what you want me to speak: ")

    if speak != 'q':
        engine.say(speak)
        engine.runAndWait()
    
    else:
        tell = "Thank you for using the Robo Speaker"
        engine.say(tell)
        engine.runAndWait()
        break

