from tkinter import *


root = Tk()

# GUI ( Graphical User Interface)
# Add label
# theLabel = Label(root, text="This is a label")
# theLabel.pack()
#
# second_label = Label(root, text="This is an other label")
# second_label.pack()
#
#
# # Add a button
# the_button = Button(None, text="Click me!", fg="Blue")
# the_button.pack(fill=X)
#
# the_button2 = Button(None, text="Hit me!", fg="Red")
# the_button2.pack(side=RIGHT, fill=Y)
#
# # Frame
# topFrame = Frame(root)
# topFrame.pack()
#
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# the_button3 = Button(topFrame, text="Button 3", fg="Purple")
# the_button3.pack()
#
# the_button4 = Button(bottomFrame, text = "Button 4", fg="Orange")
# the_button4.pack(side=LEFT)
#
# the_button5 = Button(bottomFrame, text = "Button 5", fg="Green")
# the_button5.pack(side=RIGHT)

# Grid layout
label1 = Label(root, text="Label 1")
label2 = Label(root, text="Label 2")
label3 = Label(root, text="Label 3")
label4 = Label(root, text="Label 4")


label1.grid(row=0, column=0)
label2.grid(row=0, column = 1)
label3.grid(row=1, column= 0)
label4.grid(row=1, column=1)

# Entries and Check buttons
label5 = Label(root, text="Name: ")
label5.grid(row=3, column= 0)

name_entry = Entry(root)
name_entry.grid(row=3, column=1)

password = Label(root, text="Password: ")
password.grid(row=4, column=0)

password_entry = Entry(root)
password_entry.grid(row=4,column=1 )

check_button = Checkbutton(root, text="Remember this guy !")
check_button.grid(row=5,column=0, columnspan=2, sticky="E")

# Click action
def sayHi():
    print("Hello from the button")

def callback(event):
    print("Clicked at: {},{}".format(event.x, event.y))

def leftMouse(e):
    print("Left mouse is clicked")

def rightMouse(e):
    print("Right mouse is clicked")

def scroll(e):
    print("Scrolled !")

def leftArrow(e):
    print("Left Arrow pressed")

def rightArrow(e):
    print("Right Arrow pressed")

def returnPress(e):
    print("Pressed Enter !")

clickBut = Button(root, text="Click and see !", command=sayHi)
clickBut.grid(row=6, column=1)

clickBut2 = Button(root, text="Hit this !")
clickBut2.bind("<Button-1>", callback)
clickBut2.grid(row=7, column=2)

root.geometry("500x500")

root.bind("<Button-1>", leftMouse)
root.bind("<Button-2>", scroll)
root.bind("<Button-3>", rightMouse)
root.bind("<Left>", leftArrow)
root.bind("<Right>", rightArrow)
root.bind("<Return>", returnPress)





root.mainloop()
