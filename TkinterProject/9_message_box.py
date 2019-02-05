from tkinter import *
import tkinter.messagebox
#initialize the root window
root = Tk()


#############################
# 9. Message box
#############################

#http://effbot.org/tkinterbook/tkinter-standard-dialogs.htm

tkinter.messagebox.showinfo("Information", "Do you know that this is a message from the future !")

answer = tkinter.messagebox.askquestion("Information", "Do you know believe me ?")

if answer == "yes":
    tkinter.messagebox.showinfo("Cool","You're so cool !")

elif answer == "no":
    tkinter.messagebox.showerror("Error", "WTF ?")


# Keep the window runing until user closes it
root.mainloop()
