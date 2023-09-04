import time
from tkinter import *


def pop_window(title,message,path):
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    g = Label(root, text=m, width=120, height=10)
    g.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    root.iconbitmap('clock.ico')
    mainloop()


def countdown():
    user = int(input("Please enter time to countdown in seconds: "))
    while user:
        mins,secs=divmod(user,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer,end = "\r")
        time.sleep(1)
        user -= 1
    #return "Times up!"
    return pop_window("Countdown Timer!","Times up!","Set a timer again!")
    
    
print(countdown())
