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
import os
import shutil
import time
import viewlogs
from tkintertable import TableCanvas, TableModel
import threading


cap = cv2.VideoCapture(1)
class gui:
    def open_video_show(self):
        global cap
        if self.loclavideoststus:
            if not cap.isOpened():
                cap = cv2.VideoCapture(self.path)
            _, self.frame = cap.read()
            cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            imgtk = ImageTk.PhotoImage(Image.fromarray(cv2image))
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)
            self.lmain.after(1, self.open_video_show)
           
        
    def video_show(self):
        global cap
        
        if (self.stopped):
            if not cap.isOpened():
                cap = cv2.VideoCapture(1)
            _, self.frame = cap.read()
            cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)
            self.lmain.after(1, self.video_show)
        
    def video_process(self):
        while(self.status):
            if self.e.wait():
                time.sleep(60)
                main(self.frame)
              
                
    def exit(self):
        global cap
        cap.release()
        self.root.destroy()
        self.stopped=False
        self.status=False
    def view_log(self):
        viewlogs.view()
    
    def clear_log(self):
        try:
            shutil.rmtree(r"logs/images")
            open(r"logs/log.txt", 'w').close()
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        os.mkdir(r"logs/images")
    
    def video_stream(self):
        self.stopped=True
        self.loclavideoststus=False
        cap.release()
        self.video_show() 
        time.sleep(10)
        self.e.set()
        if not self.t2.is_alive():
            self.t2.start()
            
        
    def onOpenVideo(self):
        global cap
        self.loclavideoststus=True
        self.stopped=False
        cap.release()
        self.path=filedialog.askopenfilename(filetypes=[("Video File",'.mp4'),("All Files",'.*')])
        if  self.path:
            self.open_video_show()
            time.sleep(10)
            self.e.set()
            if not (self.t2.is_alive()):
                self.t2.start()
        else:
            im = Image.open("trainData/no_display.jpg")
            tkimage = ImageTk.PhotoImage(im)
            self.lmain.image = tkimage
            self.lmain.configure(image=tkimage)
            self.lmain.grid()
       
        
        
          
    def onOpen(self):
        global cap
        cap.release()
        self.loclavideoststus=False
        
        self.stopped=False
        self.e.clear()
        
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg'),("All Files",'.*')])
        if  path:
            try:
                im = Image.open(path)
                img = cv2.imread(path)
                resize=im.resize((400,400),Image.ANTIALIAS)
                tkimage = ImageTk.PhotoImage(resize)
                self.lmain.imgtk = tkimage
                self.lmain.configure(image=tkimage)
                main(img) 
            except IOError:
                print('An error occurred trying to read the file.')
        else:
            im = Image.open("trainData/no_display.jpg")
            tkimage = ImageTk.PhotoImage(im)
            self.lmain.image = tkimage
            self.lmain.configure(image=tkimage)
            self.lmain.grid()
       
    def onTrain(self):
        global cap
        cap.release()
        self.loclavideoststus=False
        self.stopped=False
        path=filedialog.askopenfilename(filetypes=[("Image File",'.png'),("All Files",'.*')])
        if  path:
            tData(path) 
        else:
            im = Image.open("trainData/no_display.jpg")
            tkimage = ImageTk.PhotoImage(im)
            self.lmain.image = tkimage
            self.lmain.configure(image=tkimage)
            self.lmain.grid()
               
        
    def __init__(self,frame=None):
        self.stopped=None
        self.root = Tk()
        self.root.title("NoParkingVehicleDetection")
        self.root.geometry("600x400")
        self.frame= None
        self.loclavideoststus=None
        self.t2=threading.Thread(target=self.video_process,args=())
        self.e = threading.Event()
        top = Frame(self.root, borderwidth=2, relief="solid")
        top.pack(side="top", expand=True, fill="both")
        self.lmain = Label(top)
        im = Image.open("trainData/no_display.jpg")
        tkimage = ImageTk.PhotoImage(im)
        self.lmain.image = tkimage
        self.lmain.configure(image=tkimage)
        self.lmain.grid()
        self.status=True
        root_menu=Menu(self.root)
        self.root.config(menu=root_menu)
        file_menu=Menu(root_menu)
        log_menu=Menu(root_menu)
        root_menu.add_cascade(label="File",menu=file_menu)
        root_menu.add_cascade(label="Logs",menu=log_menu)
        log_menu.add_command(label="View Logs",command=self.view_log)
        log_menu.add_command(label="Clear All Logs",command=self.clear_log)
        file_menu.add_command(label="Open Image",command=self.onOpen)
        file_menu.add_command(label="Train Data",command=self.onTrain)
        file_menu.add_command(label="Open Video",command=self.onOpenVideo)
        file_menu.add_command(label="Live Stream",command=self.video_stream)
        file_menu.add_command(label="Exit",command=self.exit)
        self.root.mainloop() 
                   
