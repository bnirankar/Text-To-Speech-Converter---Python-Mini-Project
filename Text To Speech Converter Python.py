#Complete Video Tutorial Is Available on Youtube
#Youtube-- Brain Flicks
#Channel Link-- youtube.com/nirankarnathsingh
#video Link -- https://youtu.be/Q5kd0R61JBo
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[int(input('Choose your assistant\n1:DAVID\n2:ZIRA\nEnter: '))-1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
print('Commands\n1.To Read\n2.To Quit')
while True:
    x=int(input('Commands\n1.To Read\n2.To Quit\nEnter: '))
    if x==1:
        y=int(input('1.Enter a File path to read\n2.Enter text to read\nEnter: '))
        if y==1:
            fh=open(input('Enter path: ')).read()
            print(fh)
            speak(fh)
                
        elif y==2:
            t=input('Enter text:\n')
            speak(t)
    else:
        break

