from tkinter import *

#initialize the root window
root = Tk()

########################################
# 2. Buttons ( Layout, text, foreground)
#########################################
# For now we have not set up a layout, so put it None for now
# The color migh be different in different OS
tk_button = Button(None, text = "Click here", fg="Blue")
tk_button.pack()

second_button = Button(None, text="Click here too", fg="Red")
second_button.pack()



# Keep the window runing until user closes it
root.mainloop()
