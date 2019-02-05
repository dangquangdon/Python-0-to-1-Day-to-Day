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

########################################
# 2. Buttons ( Layout, text, foreground)
#########################################
# For now we have not set up a layout, so put it None for now
# The color migh be different in different OS
tk_button = Button(None, text = "Click here", fg="Blue")
tk_button.pack()

second_button = Button(None, text="Click here too", fg="Red")
second_button.pack()

#############################
# 3. Layout, Frame
#############################
tk_topFrame = Frame(root)
tk_topFrame.pack()

tk_botFrame = Frame(root)
tk_botFrame.pack(side=BOTTOM)

# Since we have only two frames, and sepcified one is BOTTOM
# Python will understand that the other one is TOP
# If we have more frames, we might have to specify more

button3 = Button(tk_topFrame, text="Button 3", fg="Yellow")
button3.pack(side=RIGHT)

button4 = Button(tk_topFrame, text="Button 4", fg="Purple")
button4.pack(side=LEFT)

button5 = Button(tk_botFrame, text="Button 5", fg="Orange")
button5.pack(side=LEFT)

button6 = Button(tk_botFrame, text="Button 6", fg="Green")
button6.pack(side=RIGHT)


######################
# 4.Fill
######################




# Keep the window runing until user closes it
root.mainloop()
