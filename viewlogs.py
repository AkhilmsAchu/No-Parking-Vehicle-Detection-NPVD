import tkinter as tk
import tkinter
from tkinter import *
import csv
from PIL import ImageTk, Image

def view():
    parent = tk.Toplevel()
    parent.title("Logs")
    
    canvas = tk.Canvas(parent)
    scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    
    frame = tk.Frame(canvas)
    # group of widgets
    frame1 = tk.Frame(frame)
    label = tk.Label(frame1, width = 10, height = 2, \
                                       text = "Image", relief = tk.RIDGE).pack(side=tk.LEFT)
    label = tkinter.Label(frame1, width = 10, height = 2, \
                                       text = "Numberplate", relief = tk.RIDGE).pack(in_=frame1, side=tk.LEFT)
    label = tkinter.Label(frame1, width = 10, height = 2, \
                                       text = "Date", relief = tk.RIDGE).pack(in_=frame1, side=tk.LEFT)
    label = tkinter.Label(frame1, width = 10, height = 2, \
                                       text = "Time", relief = tk.RIDGE).pack(in_=frame1, side=tk.LEFT)
    frame1.pack(side=tk.TOP, expand=True)
    frame2 = tk.Frame(frame)
    with open(r"logs/log.txt", newline = "") as file:
           reader = csv.reader(file)
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
                      panel = tkinter.Label(frame2, image=img)
                      panel.image = img
                      panel.grid(row = r, column = c)
                                      
                      #tkimage = ImageTk.PhotoImage(im)
                      #lmain.image = tkimage
                      #lmain.configure(image=tkimage)
                      #lmain.grid(row = r, column = c)
                      c += 1
                  else:
                     # i've added some styling
                     label = tkinter.Label(frame2, width = 10, height = 2, \
                                           text = row, relief = tkinter.RIDGE)
                     label.grid(row = r, column = c)
                     c += 1
              r += 1
              frame2.pack(side=tk.TOP, expand=True)
        
           
    # put the frame in the canvas
    canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    canvas.update_idletasks()
    
    canvas.configure(scrollregion=canvas.bbox('all'), 
                     yscrollcommand=scroll_y.set)
                     
    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')
    parent.mainloop()
#view()