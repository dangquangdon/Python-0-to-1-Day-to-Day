from tkinter import *

#initialize the root window
root = Tk()


#############################
# 10. Dropdown Menu
#############################


# initialize menu

def someFunc():
    print("This is some function")


mainMenu = Menu(root)
root.configure(menu=mainMenu)

subMenu = Menu(mainMenu)

mainMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Some Func", command=someFunc)
subMenu.add_separator()
subMenu.add_command(label="New tab", command=someFunc)


# Keep the window runing until user closes it
root.mainloop()
