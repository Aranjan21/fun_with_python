#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from compress import compress, decompress
from tkinter import filedialog

'''Below function helps to choose the file from local directory'''
def choose_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Choose the file to compress")
    return filename


def compression(inputfile,outputfile):
    compress(inputfile,outputfile)
window = tk.Tk()

window.title("File Compression App")
window.geometry("600x400")

label = Label(window,text="File to be compressed")
label.grid(row=0, column=0)
input_entry = Entry(window)
input_entry.grid(row=0,column=1)

label = Label(window, text="Compressed File")
label.grid(row=1,column=0)
output_entry = Entry(window)
output_entry.grid(row=1,column=1)

compress_button = tk.Button(window,text="Compress",command=lambda:compression(input_entry.get(),output_entry.get()))
compress_button.grid(row=2,column=1)
window.mainloop()
