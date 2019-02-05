from tkinter import *

#initialize the root window
root = Tk()


#############################
# 5. Grid Layout
#############################

# Grid layout will help us to place widgets easier
# Like excel

label_1 = Label(root, text="Label 1")

label_2 = Label(root, text="Label 2")

label_3 = Label(root, text="Label 3")

# In here we don't use pack() anymore
# Because pack() work on the basics of sides (top, bottom, left, right)
# Grid works on the basics of rows and columns

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=1, column=0)




# Keep the window runing until user closes it
root.mainloop()
