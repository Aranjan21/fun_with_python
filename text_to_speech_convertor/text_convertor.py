#!/usr/bin/env python3
from gtts import gTTS
import os
from tkinter import *

window = Tk()

def textToSpeech():
    text = input_entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('converted.mp3')
    os.system("afplay converted.mp3")

window.title("Text Convertor App")
window.geometry("600x400")

label = Label(window, text="Enter the text")
label.grid(row=0,column=0)

input_entry = Entry(window)
input_entry.grid(row=0,column=1)

convert_button = Button(window,text="Convert",command=textToSpeech)
convert_button.grid(row=1,column=1)

window.mainloop()
