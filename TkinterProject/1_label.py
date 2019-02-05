from tkinter import *


#initialize the root window
root = Tk()
#######################
# 1. Adding label
######################
tk_label = Label(root, text="This is a label")
# If we run it right away, there is nothing showing
# we have to add it by doing this
tk_label.pack()

second_label = Label(root, text="This is a second label")
second_label.pack()

# Keep the window runing until user closes it
root.mainloop()
