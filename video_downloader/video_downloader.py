#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

def download():
    file_path = url_path.cget("text")
    video_path = url_entry.get()
    video = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(video)
    video_clip.close()
    shutil.move(video, file_path)
    print("Download Completed.....")

def get_path():
    path = filedialog.askdirectory()
    url_path.config(text=path)


root = Tk()
root.title('Video downloader')
canvas = Canvas(root, width=400,height=300)
canvas.pack()

#App Label
app_label = Label(root,text='Video Downloader',fg='blue',font=('Arail',20))
canvas.create_window(200,20,window=app_label)

#Entry to accept video URL
url_label = Label(root,text='Enter Youtube Video URL')
canvas.create_window(200,80,window=url_label)

url_entry = Entry(root)
canvas.create_window(200,100,window=url_entry)

#Folder to download the videos
url_path = Label(root, text='Select path to download')
canvas.create_window(200,150, window=url_path)

#Select button
path_button = Button(root,text='Select',command=get_path)
canvas.create_window(200,180, window=path_button)

#downlaod button
download_button = Button(root,text='download',command=download)
canvas.create_window(200,230, window=download_button)

root.mainloop()
