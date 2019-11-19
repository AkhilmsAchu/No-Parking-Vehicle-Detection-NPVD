# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:51:34 2019

@author: ACHU
"""

import tkinter
import csv
from PIL import ImageTk, Image
root = tkinter.Tk()

# open file
with open(r"logs/log.txt", newline = "") as file:
   reader = csv.reader(file)
   

   # r and c tell us where to grid the labels
   label = tkinter.Label(root, width = 10, height = 2, \
                               text = "Image", relief = tkinter.RIDGE)
   label.grid(row = 0, column = 0)
   label = tkinter.Label(root, width = 10, height = 2, \
                               text = "Numberplate", relief = tkinter.RIDGE)
   label.grid(row = 0, column = 1)
   label = tkinter.Label(root, width = 10, height = 2, \
                               text = "Date", relief = tkinter.RIDGE)
   label.grid(row = 0, column = 2)
   label = tkinter.Label(root, width = 10, height = 2, \
                               text = "Time", relief = tkinter.RIDGE)
   label.grid(row = 0, column = 3)
   r = 1
   for col in reader:
      c = 0
      for row in col:
          if c==0:
              lmain = tkinter.Label(root,width = 100, height = 70)
              im = Image.open(r"logs/images/"+row)
              tkimage = ImageTk.PhotoImage(im)
              lmain.image = tkimage
              lmain.configure(image=tkimage)
              lmain.grid(row = r, column = c)
              c += 1
          else:
             # i've added some styling
             label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)
             label.grid(row = r, column = c)
             c += 1
      r += 1

root.mainloop()