# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:51:34 2019

@author: ACHU
"""
import os
import tkinter
import csv
import cv2
from PIL import ImageTk, Image

def view():
    root1 = tkinter.Toplevel()
    root1.title("Logs")

    # open file

    with open(r"logs/log.txt", newline = "") as file:
       reader = csv.reader(file)
       
    
       # r and c tell us where to grid the labels
       label = tkinter.Label(root1, width = 10, height = 2, \
                                   text = "Image", relief = tkinter.RIDGE)
       label.grid(row = 0, column = 0)
       label = tkinter.Label(root1, width = 10, height = 2, \
                                   text = "Numberplate", relief = tkinter.RIDGE)
       label.grid(row = 0, column = 1)
       label = tkinter.Label(root1, width = 10, height = 2, \
                                   text = "Date", relief = tkinter.RIDGE)
       label.grid(row = 0, column = 2)
       label = tkinter.Label(root1, width = 10, height = 2, \
                                   text = "Time", relief = tkinter.RIDGE)
       label.grid(row = 0, column = 3)
       r = 1
       for col in reader:
          c = 0
          for row in col:
              if c==0:
                  print(row)
                  #lmain = tkinter.Label(root1,width = 100, height = 70)
                  img = Image.open(r"logs/images/"+row)
                  
                  #img = Image.open(x)
                  img = img.resize((50, 50), Image.ANTIALIAS)
                  img = ImageTk.PhotoImage(img)
                  panel = tkinter.Label(root1, image=img)
                  panel.image = img
                  panel.grid(row = r, column = c)
                                  
                  #tkimage = ImageTk.PhotoImage(im)
                  #lmain.image = tkimage
                  #lmain.configure(image=tkimage)
                  #lmain.grid(row = r, column = c)
                  c += 1
              else:
                 # i've added some styling
                 label = tkinter.Label(root1, width = 10, height = 2, \
                                       text = row, relief = tkinter.RIDGE)
                 label.grid(row = r, column = c)
                 c += 1
          r += 1
    
    root1.mainloop()
#view()