from tkinter import *
from gtts import gTTS 
from playsound import playsound
import random
import os

# Tk() to initialized tkinter which will be used for GUI
# geometry() used to set the width and height of the window
# configure() used to access window attributes
# bg will used to set the color of the background
# title() set the title of the window

root = Tk()
root.geometry("350x300") 
root.configure(bg='ghost white')
root.title("DataFlair - TEXT TO SPEECH")

# Label() widget is used to display one or more than one line of text that users can’t able to modify.

# root is the name which we refer to our window
# text which we display on the label
# font in which the text is written
# pack organized widget in block
# Msg is a string type variable
# Entry() used to create an input text field
# textvariable used to retrieve the current text to entry widget
# place() organizes widgets by placing them in a specific position in the parent widget

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="UVAIS AHMAD", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

# Message variable will stores the value of entry_field
# text is the sentences or text to be read.
# lang takes the language to read the text. The default language is English.
# slow use to reads text more slowly. The default is False.
# As we want the default value of lang, so no need to give that to gTTS.

# speech stores the converted voice from the text
# speech.save(‘DataFlair.mp3’) will saves the converted file as DataFlair as mp3 file
# playsound() used to play the sound

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    r="audio"+str(random.randint(1,100))+".mp3"
    speech.save(r)
    playsound(r)
    os.remove(r)

# root.destroy() will quit the program by stopping the mainloop().

def Exit():
    root.destroy()

# Reset function set Msg variable to empty strings.

def Reset():
    Msg.set("")

# Button() widget used to display button on the window 

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

# root.mainloop() is a method that executes when we want to run our program.

root.mainloop()