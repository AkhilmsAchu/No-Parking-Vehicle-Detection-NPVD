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
import time
from tkintertable import TableCanvas, TableModel

#import tkFileDialog
import threading
class gui:
    
    
    def video_show(self):
        if self.cap.isOpened():
            _, self.frame = self.cap.read()
            
        else:
           self.cap = cv2.VideoCapture(0)
           cap.set(CV_CAP_PROP_FRAME_WIDTH,100)
           cap.set(CV_CAP_PROP_FRAME_HEIGHT,100)
           self.t1.start()
           self.t2.start()
        cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        #resize=img.resize((400,400),Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(1, self.video_show)
        
    def video_process(self):
        while(self.stopped):
            preprocess(self.frame)
        
        #contours= extract_contours(threshold_img)
        #cleanAndRead(frame,contours)
    def video_stream(self):
        
        self.t1.start()
        time.sleep(10)
        self.t2.start()
       
    def exit(self):
        self.cap.release()
        self.root.destroy()
        self.stopped=False
       
    def onOpen(self):
        self.cap.release()
        
        
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'),("All Files",'.*')])
        im = Image.open(path)
        img = cv2.imread(path)
        resize=im.resize((400,400),Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resize)
        self.lmain.imgtk = tkimage
        self.lmain.configure(image=tkimage)
        preprocess(img)       
        #ftypes = [('Image files', '*.jpg'), ('All files', '*')]
        #fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        #imgtk = Image.open(fileName)
        # = imgtk
        #self.lmain.configure(image=imgtk)
    
    def __init__(self,frame=None):
        self.stopped=True
        self.root = Tk()
        self.root.title("NoParkingVehicleDetection")
        self.root.geometry("600x400")

        #self.frame = frame
        self.cap = cv2.VideoCapture(0)
        self.t1=threading.Thread(target=self.video_show,args=())
        self.t2=threading.Thread(target=self.video_process,args=())
        

        top = Frame(self.root, borderwidth=2, relief="solid")
        top.pack(side="top", expand=True, fill="both")
        bottom = Frame(self.root, borderwidth=2, relief="solid")
        bottom.pack(side="bottom", expand=True, fill="both")
        # Create a frame
        #app = Frame(self.root, bg="white")
        #app.grid()
        # Create a label in the frame
        self.lmain = Label(top)
        self.lmain.grid()
        #self.cap = cv2.VideoCapture(0)
        # Capture from camera

        table = TableCanvas(bottom)
        table.show()
        
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
            
        
