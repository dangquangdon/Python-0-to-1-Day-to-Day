from tkinter import *

#initialize the root window
root = Tk()

#############################
# 4. Fill
#############################

#If we resize the window (make it bigger or smaller, the size of the buttons doesn't change)
# Therefore we use fill
button1 = Button(None, text="Button 1", fg="Yellow")
button1.pack()

button2 = Button(None, text="Button 2", fg="Purple")
# fill X axis
button2.pack( fill=X)

button3 = Button(None, text="Button 3", fg="Orange")
# Fill along Y axis
button3.pack(side=RIGHT, fill=Y)

button4 = Button(None, text="Button 4", fg="Green")
button4.pack()







# Keep the window runing until user closes it
root.mainloop()
