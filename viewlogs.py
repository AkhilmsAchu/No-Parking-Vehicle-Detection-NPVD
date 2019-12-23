import tkinter as tk
import tkinter
from tkinter import *
import csv
import os
from PIL import ImageTk, Image



def operation(text):
    os.remove(r"logs/images/"+text)
    with open(r"logs/log.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if text not in line:
                f.write(line)
        f.truncate()
    parent.destroy()
    view()
    
def logview(text,num):
    print(text)
    parent1 = tk.Toplevel()
    parent1.title("Parking Details")
    parent1.geometry("600x400")
    frame = tk.Frame(parent1)
    img = Image.open(r"logs/images/"+text)
    img = img.resize((240, 180), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tkinter.Label(frame, image=img)
    panel.image = img
    panel.grid(row = 1, column = 1,columnspan=2)
    
    
    label1 = tkinter.Label(frame, width = 15, height = 2, \
                                           text = "Vehicle Number", relief = tkinter.RIDGE)
    label1.grid(row = 3, column = 1)
    
    label2 = tkinter.Label(frame, width = 10, height = 2, \
                                           text = "Date", relief = tkinter.RIDGE)
    label2.grid(row = 4, column = 1)
    label3 = tkinter.Label(frame, width = 10, height = 2, \
                                           text = "Time", relief = tkinter.RIDGE)
    label3.grid(row = 5, column = 1)
    
    label11 = tkinter.Label(frame, width = 10, height = 2, \
                                           text = num, relief = tkinter.RIDGE)
    label11.grid(row = 3, column = 2)
    
    label22 = tkinter.Label(frame, width = 10, height = 2, \
                                           text = text[0:10], relief = tkinter.RIDGE)
    label22.grid(row = 4, column = 2)
    label33 = tkinter.Label(frame, width = 10, height = 2, \
                                           text = text[11:19], relief = tkinter.RIDGE)
    label33.grid(row = 5, column = 2)
    btnp=tkinter.Button(frame, text="Print").grid(row = 7, column = 1,columnspan=2)
                      
    frame.pack()
    parent1.mainloop()


def view():
    global parent
    parent = tk.Toplevel()
    parent.title("Logs")
    parent.geometry("600x400")
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
    label = tkinter.Label(frame1, width = 20, height = 2, \
                                       text = "Operation", relief = tk.RIDGE).pack(in_=frame1, side=tk.LEFT)
    frame1.pack(side=tk.TOP, expand=True)
    frame2 = tk.Frame(frame)
    with open(r"logs/log.txt", newline = "") as file:
           reader = csv.reader(file)
           r = 1
           num=""
           for col in reader:
              c = 0
              current=""
              for row in col:
                  if c==0:
                      print(row)
                      #lmain = tkinter.Label(root1,width = 100, height = 70)
                      img = Image.open(r"logs/images/"+row)
                      current=row
                      #img = Image.open(x)
                      img = img.resize((50, 50), Image.ANTIALIAS)
                      img = ImageTk.PhotoImage(img)
                      panel = tkinter.Label(frame2, image=img)
                      panel.image = img
                      panel.grid(row = r, column = c)
                      c += 1
                  elif c==4:
                      btnp=tkinter.Button(frame2, text="Delete",command=lambda current=current:operation(current), width = 10, height = 2).grid(row=r,column=c)
                      c += 1
                      btnp=tkinter.Button(frame2, text="View",command=lambda current=current,num=num:logview(current,num), width = 10, height = 2).grid(row=r,column=c)
                      c += 1
                  else:
                     if c==1:
                         num=row
                          
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
    