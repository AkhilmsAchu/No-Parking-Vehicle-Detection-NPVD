# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:58:04 2019

@author: ACHU
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from Main import *
from GenData import *
import cv2
import time
import viewlogs
from tkintertable import TableCanvas, TableModel

#import tkFileDialog
import threading
class gui:
    
    def open_video_show(self):
        if self.loclavideoststus:
            if (self.cap.isOpened()==False):
               self.cap = cv2.VideoCapture(self.path)
            _, self.frame = self.cap.read()
            cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            imgtk = ImageTk.PhotoImage(Image.fromarray(cv2image))
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)
            self.lmain.after(1, self.open_video_show)
           
        
    def video_show(self):
        if (self.stopped):
            if self.cap.isOpened():
                _, self.frame = self.cap.read()
                
            else:
               self.cap = cv2.VideoCapture(0)
               #self.cap.set(CV_CAP_PROP_FRAME_WIDTH,100)
               #self.cap.set(CV_CAP_PROP_FRAME_HEIGHT,100)
               #self.t1.start()
               #self.t2.start()
            cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            #resize=img.resize((400,400),Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image=img)
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)
            self.lmain.after(1, self.video_show)
        
    def video_process(self):
        while(self.stopped):
            main(self.frame)
        
        #contours= extract_contours(threshold_img)
        #cleanAndRead(frame,contours)
    def exit(self):
        loclavideoststus=False
        self.cap.release()
        self.root.destroy()
        self.stopped=False
        
    def view_log(self):
        viewlogs.view()
    
    def video_stream(self):
        self.stopped=True
        self.loclavideoststus=False
        print(self.t1.is_alive())
        self.video_show() 
        time.sleep(10)
        if not self.t2.is_alive():
            self.t2.start()
        else:
            self.video_process()
       
        
    def onOpenVideo(self):
        self.loclavideoststus=True
        self.stopped=True
        self.cap.release()
        self.path=filedialog.askopenfilename(filetypes=[("Video File",'.mp4'),("All Files",'.*')])
        #self.cap = cv2.VideoCapture(path)
        #_, self.frame = self.cap.read()
#        
#        self.t3.start()
#        time.sleep(10)   
#        self.t2.start()
        #self.video_process()
        self.open_video_show() 
        
        time.sleep(10)
        
        if not self.t2.is_alive():
            self.t2.start()
        else:
            self.video_process()
            
    def onOpen(self):
        self.cap.release()
        self.loclavideoststus=False
        
        self.stopped=False
        
        
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'),("All Files",'.*')])
        im = Image.open(path)
        img = cv2.imread(path)
        resize=im.resize((400,400),Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resize)
        self.lmain.imgtk = tkimage
        self.lmain.configure(image=tkimage)
        main(img)       
        #ftypes = [('Image files', '*.jpg'), ('All files', '*')]
        #fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        #imgtk = Image.open(fileName)
        # = imgtk
        #self.lmain.configure(image=imgtk)
    
    def onTrain(self):
        self.cap.release()
        self.loclavideoststus=False
        self.stopped=False
        path=filedialog.askopenfilename(filetypes=[("Image File",'.png'),("All Files",'.*')])
        tData(path)       
        
    def __init__(self,frame=None):
        self.stopped=None
        self.root = Tk()
        self.root.title("NoParkingVehicleDetection")
        self.root.geometry("600x400")
        self.frame= None
        self.loclavideoststus=None
        
        #self.frame = frame
        self.cap = cv2.VideoCapture(0)
        self.t1=threading.Thread(target=self.video_show,args=())
        self.t2=threading.Thread(target=self.video_process,args=())
        self.t3=threading.Thread(target=self.open_video_show,args=())

        top = Frame(self.root, borderwidth=2, relief="solid")
        top.pack(side="top", expand=True, fill="both")
        bottom = Frame(self.root, borderwidth=2, relief="solid")
        bottom.pack(side="bottom", expand=True, fill="both")
        # Create a frame
        #app = Frame(self.root, bg="white")
        #app.grid()
        # Create a label in the frame
        self.lmain = Label(top)
        
        im = Image.open("trainData/no_display.jpg")
        
#        self.lmain=ImageTk.PhotoImage(im)
#        self.lmain.imgtk = tkimage
        
        tkimage = ImageTk.PhotoImage(im)
        self.lmain.image = tkimage
        self.lmain.configure(image=tkimage)
        self.lmain.grid()
        # Capture from camera

        table = TableCanvas(bottom)
        table.show()
        
        root_menu=Menu(self.root)
        self.root.config(menu=root_menu)
        file_menu=Menu(root_menu)
        log_menu=Menu(root_menu)
        root_menu.add_cascade(label="File",menu=file_menu)
        root_menu.add_cascade(label="Logs",menu=log_menu)
        log_menu.add_command(label="View Log",command=self.view_log)
        log_menu.add_command(label="Delete Log",command=self.onOpen)
        file_menu.add_command(label="Open Image",command=self.onOpen)
        file_menu.add_command(label="Train Data",command=self.onTrain)
        file_menu.add_command(label="Open Video",command=self.onOpenVideo)
        file_menu.add_command(label="Live Stream",command=self.video_stream)
        file_menu.add_command(label="Exit",command=self.exit)
        # function for video streaming
        
        #video_stream()
        self.root.mainloop() 
                   
