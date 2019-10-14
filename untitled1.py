# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:31:56 2019

@author: ACHU
"""

import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk

video_name = "test.mkv" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

if __name__ == "__main__":

    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()