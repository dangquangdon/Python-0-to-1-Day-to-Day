from tkinter import *

root = Tk()

formula=""
equation = StringVar()

calculation = Label(root, textvariable=equation)

equation.set("0")

calculation.grid(columnspan=4)


#Creating buttons & functions

def buttonPress(num):
    # We create a gloabl variable that will be updated whenever the button is pressed
    global formula
    formula = formula + str(num)
    equation.set(formula)

def equalBut():
    # We will need to use eval() to evaluate equation string and do the math
    global formula
    total = str(eval(formula))
    equation.set(total)
    formula=""

def clearBut():
    global formula
    formula = ""
    equation.set(formula)

button_1 = Button(root, text="1", command=lambda: buttonPress(1))
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", command=lambda: buttonPress(2))
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", command=lambda: buttonPress(3))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", command=lambda: buttonPress(4))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", command=lambda: buttonPress(5))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", command=lambda: buttonPress(6))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", command=lambda: buttonPress(7))
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", command=lambda: buttonPress(8))
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", command=lambda: buttonPress(9))
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0", command=lambda: buttonPress(0))
button_0.grid(row=4, column=0)

button_plus = Button(root, text="+", command=lambda: buttonPress("+"))
button_plus.grid(row=1, column=3)

button_minus = Button(root, text="-", command=lambda: buttonPress("-"))
button_minus.grid(row=2, column=3)

button_multi = Button(root, text="*", command=lambda: buttonPress("*"))
button_multi.grid(row=3, column=3)

button_divide = Button(root, text="/", command=lambda: buttonPress("/"))
button_divide.grid(row=4, column=3)

button_equal = Button(root, text="=", command=equalBut)
button_equal.grid(row=4, column=2)


button_clear = Button(root, text="C", command=clearBut)
button_clear.grid(row=4, column=1)

root.mainloop()
