from turtle import *
import math

def pentagon():
    color("blue","red")
    begin_fill()
    while True:
    
        forward(100)
        left(45)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

def star():
    color("gold","gold")
    begin_fill()
    penup()
    goto(-100,0)
    pendown()
    for i in range(5):
        forward(200)
        right(144)
    end_fill()
    done()

def curve():
    #speed up the curve speed
    speed(1000)

    #make a curve for the love
    for i in range (200):
        right(1)
        forward(1)

def love():
    
    #fill colour
    color("red","red")

    begin_fill()
    
    #start
    left(140)
    forward(114) 
    
    #curve left and right
    curve()
    left(120)
    curve()

    #end
    forward(114)
    end_fill()
    done()

def circle():
    speed(1000)

    for i in range(360):
        right(1)
        forward(1)
    done()

circle()
