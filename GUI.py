from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.title("text to speech")

label = Label(root ,text="Text To Speech" , font="Tahoma 35 bold italic" , fg="indianred")
label.pack(pady=26)

label2 = Label(root, text="Enter your text" ,font="Tahoma 25 bold" , fg="olive")
label2.pack(padx=30 ,pady=30 ,ipady=5 ,anchor="w")

entry = Entry(root ,width=50)
entry.pack(ipady=5 ,padx=30 ,pady=10 ,fill=X ,anchor="center")

def playVoice() :
    mytext = entry.get()
    myjob = gTTS(text=mytext)
    if os.path.exists("sound.mp3") :
        os.remove("sound.mp3")
    myjob.save('sound.mp3')
    playsound('sound.mp3')

btn1 = Button(root ,text="Play" ,font="bold" ,bg="sandybrown" ,fg="black" ,width=18 ,command=playVoice)
btn1.pack(side=LEFT ,padx=20 ,pady=40 ,ipady=5 ,anchor="sw" ,fill=X ,expand=True)

def exitGUI() :
    root.quit()

btn2 = Button(root ,text="Exit" ,font="bold" ,bg="red" ,fg="black" ,width=18 ,command=exitGUI)
btn2.pack(side=LEFT ,padx=20 ,pady=40 ,ipady=5 ,anchor="s" ,fill=X ,expand=True)

def deleteTXT() :
    entry.delete(0,END)

btn3 = Button(root ,text="Set" ,font="bold" ,bg="lightseagreen" ,fg="black" ,width=18 ,command=deleteTXT)
btn3.pack(side=LEFT ,padx=20 ,pady=40 ,ipady=5 , anchor="se" ,fill=X ,expand=True)

root.mainloop()