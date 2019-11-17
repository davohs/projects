import numpy as np
from tkinter import *

tk = Tk() 
canvas = Canvas(tk, width=1000, height=1000) # The animated window is 1000x1000 pixels
tk.title("Frame")

canvas.pack()
w = int(input("Width of brick: "))      
h = int(input("Height of brick: "))     # Asks user for dimensions of the individual bricks used
    # d = direction of wind
    # m = windspeed (I'm investigating a feature, where the wind speed and direction vary as a mathematical function of time, given by the user, in order to emulate a broader range of conditions)
BrickX = int(input("How long should the wall be: "))
BrickY = int(input("How high should the wall be: "))    #finds the height and width of the wall in bricks
BrickT = BrickX * BrickY
canvas.create_rectangle(0, 500, 1000, 1000, fill="green" )
brickstack = []
def BrickStack():
        
    for i in range(BrickT):     # Checks for total bricks
        brickstack.append(i)        # Assigns every brick to an index in list bricks[]
        brickstack[i] = canvas.create_rectangle(100, 500-h*i ,100+w ,(500-h)-h*i)  # Creates a rectangle .. fill="orange"
 

BrickStack()

brickstack.reverse()
W = np.arange(BrickT).reshape(BrickY, BrickX)  # Represents wall as a matrix
W = np.flip(W)



canvas.create_oval(42,50,68,46, tags ="Drone", fill = "azure")    
canvas.create_oval(72,50,100,46, tags ="Drone", fill = "azure")
canvas.create_oval(50,60,90,56, tags ="Drone", fill = "grey25")
canvas.create_rectangle(50,50,90,58, tags ="Drone", fill= "grey25")
canvas.create_oval(38,52,68,48, tags ="Drone", fill = "azure")
canvas.create_oval(72,52,102,48, tags ="Drone", fill = "azure")

 #Set of objects tagged to Drone, in order to associate them 



def MoveBricks():
    for p in range(BrickT):
        n = p//BrickX
        u = BrickX - ((brickstack[p]-2) % BrickX) -1
        b = W[n][u]-n
        
        for t in range(100 + w*(p-BrickX*n)):
            canvas.move(brickstack[p], 1, 0)
            tk.update()
        if b > 0:
            for r in range(h*b):
                canvas.move(brickstack[p], 0, 1)
                tk.update()
        else:
            for r in range(abs(h*b)):
                canvas.move(brickstack[p], 0, -1)
                tk.update()
            
MoveBricks()




canvas.mainloop()






