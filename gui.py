# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:58:04 2019

@author: ACHU
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from main import preprocess,extract_contours,cleanAndRead
import cv2
#import tkFileDialog
import threading
class gui:
    
    def video_stream(self):
        if self.cap.isOpened():
            _, frame = self.cap.read()
        else:
           self.cap = cv2.VideoCapture(0)
           
        threshold_img = preprocess(frame)
        #t1.start()
        #contours= extract_contours(threshold_img)
        #cleanAndRead(frame,contours)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(1, self.video_stream)
    def exit(self):
        self.cap.release()
        self.root.destroy()
       
    def onOpen(self):
        self.cap.release()
        
        
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
        im = Image.open(path)
        img = cv2.imread(path)
        tkimage = ImageTk.PhotoImage(im)
        self.lmain.imgtk = tkimage
        self.lmain.configure(image=tkimage)
        preprocess(img)       
        #ftypes = [('Image files', '*.jpg'), ('All files', '*')]
        #fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        #imgtk = Image.open(fileName)
        # = imgtk
        #self.lmain.configure(image=imgtk)
    
    def __init__(self):
        self.root = Tk()
        self.cap = cv2.VideoCapture(0)
        #t1=threading.Thread(target=threshold_img,args=(frame))
        # Create a frame
        app = Frame(self.root, bg="white")
        app.grid()
        # Create a label in the frame
        self.lmain = Label(app)
        self.lmain.grid()
        #self.cap = cv2.VideoCapture(0)
        # Capture from camera
        
        root_menu=Menu(self.root)
        self.root.config(menu=root_menu)
        file_menu=Menu(root_menu)
        root_menu.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="Open File",command=self.onOpen)
        file_menu.add_command(label="Live Stream",command=self.video_stream)
        file_menu.add_command(label="Exit",command=self.exit)
        # function for video streaming
        
        #video_stream()
        self.root.mainloop() 
            
        