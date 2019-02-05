from tkinter import *

#initialize the root window
root = Tk()


#############################
# 7. Click action
#############################

# 1
def printHello():
    print("Hello !")

# Once the button is clicked, the function will be executed
button_1 = Button(root, text="Click me !", command = printHello)
button_1.pack()


#BINDING FUNCTIONS
# http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# 2
def callback(event):
    print("clicked at", event.x, event.y)

# Binding just means that we bind a function to an event that happens with a widget
button_2 = Button(root, text="Click it")
button_2.bind("<Button-1>", callback)
button_2.pack()


def leftClick(event):
    print("Left Click")

def rightClick(event):
    print("Right Click")

def scroll(event):
    print("Scroll")

def leftArrow(event):
    print("Left Arrow key")

def rightArrow(event):
    print("Right Arrow key")


# Set the window size
root.geometry("500x500")

root.bind("<Button-1>", leftClick)

root.bind("<Button-2>", scroll)

root.bind("<Button-3>", rightClick)

root.bind("<Left>", leftArrow)

root.bind("<Right>", rightArrow)

# Keep the window runing until user closes it
root.mainloop()
