from tkinter import *

#initialize the root window
root = Tk()


#############################
# 8. Get data from entries
#############################

label1 = Label(root, text="Enter your math")
label1.pack()


def evaluate(event):
    data  = entry.get()
    answer.configure(text="Answer is: {}".format(str(eval(data))))
# The eval() method parses the expression passed to this method and runs python expression (code) within the program.


entry = Entry(root)
entry.bind("<Return>", evaluate)
entry.pack()


answer = Label(root)
answer.pack()




# Keep the window runing until user closes it
root.mainloop()
