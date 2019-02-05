from tkinter import *

#initialize the root window
root = Tk()

#############################
# 6. Entries & Check buttons
#############################

# Entries are text boxes where user can insert data (name, password, etc)

label1 = Label(root, text="Name: ")
label1.grid(row = 2, column=2, sticky="E")
# Add sticky to align North, South, East, West

entryBox = Entry(root)
entryBox.grid(row = 2, column= 3)


# Check buttons
# check_button = Checkbutton(root, text="Remember this guy")
# check_button.grid(row=5, column=2 , columnspan=2)


# Password field
label2 = Label(root, text="Password: ")
label2.grid(row=3, column=2, sticky="E")

entryPassword = Entry(root)
entryPassword.grid(row=3, column=3)

# Check buttons
check_button = Checkbutton(root, text="Remember Password")
check_button.grid(row=5, column=2 , columnspan=2,  sticky="W")


# Keep the window runing until user closes it
root.mainloop()
