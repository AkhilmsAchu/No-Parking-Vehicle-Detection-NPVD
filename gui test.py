# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:58:04 2019

@author: ACHU
"""

from tkinter import *
from PIL import ImageTk, Image
import cv2
class gui:
    def video_stream(self):
        _, frame = self.cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(1, self.video_stream) 
    def exit(self):
        self.app.destroy()
       
    def __init__(self):
        self.root = Tk()
        # Create a frame
        app = Frame(self.root, bg="white")
        app.grid()
        # Create a label in the frame
        self.lmain = Label(app)
        self.lmain.grid()
        self.cap = cv2.VideoCapture(0)
        # Capture from camera
        
        root_menu=Menu(self.root)
        self.root.config(menu=root_menu)
        file_menu=Menu(root_menu)
        root_menu.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="Open File",command=self.video_stream)
        file_menu.add_command(label="Live Stream",command=self.video_stream)
        file_menu.add_command(label="Exit",command=exit)
        # function for video streaming
        
        #video_stream()
        self.root.mainloop() 
            
     
gui()   