from tkinter import *


root = Tk()

formula = ""

equation = StringVar()
equation.set("0")

calculation = Label(root, textvariable = equation)
calculation.grid(row=0, columnspan = 4)


def pressBut(num):
    global formula
    if formula in ["0", "*", "+", "/"]:
        formula = str(num)
    else:
        formula = formula + str(num)
    equation.set(formula)

def equalBut():
    global formula
    result = str(eval(formula))
    equation.set(result)
    formula = result

def clearBut():
    global formula
    formula = ""
    equation.set(formula)

button1 = Button(root, text="1", padx=15, pady=15, command= lambda: pressBut(1))
button1.grid(row=1, column=0)

button2 = Button(root, text="2", padx=15, pady=15, command= lambda: pressBut(2))
button2.grid(row=1, column=1)

button3 = Button(root, text="3", padx=15, pady=15, command= lambda: pressBut(3))
button3.grid(row=1, column=2)

button4 = Button(root, text="4", padx=15, pady=15, command= lambda: pressBut(4))
button4.grid(row=2, column=0)

button5 = Button(root, text="5", padx=15, pady=15, command= lambda: pressBut(5))
button5.grid(row=2, column=1)

button6 = Button(root, text="6", padx=15, pady=15, command= lambda: pressBut(6))
button6.grid(row=2, column=2)

button7 = Button(root, text="7", padx=15, pady=15, command= lambda: pressBut(7))
button7.grid(row=3, column=0)

button8 = Button(root, text="8", padx=15, pady=15, command= lambda: pressBut(8))
button8.grid(row=3, column=1)

button9 = Button(root, text="9", padx=15, pady=15, command= lambda: pressBut(9))
button9.grid(row=3, column=2)

button0 = Button(root, text="0", padx=15, pady=15, command= lambda: pressBut(0))
button0.grid(row=4, column=0)

buttonClear = Button(root, text="C", padx=15, pady=15, command= clearBut)
buttonClear.grid(row=4, column=1)

buttonEqual = Button(root, text="=", padx=15, pady=15, command= equalBut)
buttonEqual.grid(row=4, column=2)

buttonPlus = Button(root, text="+", padx=15, pady=15, command= lambda: pressBut("+"))
buttonPlus.grid(row=1, column=3)

buttonMinus = Button(root, text="-", padx=15, pady=15, command= lambda: pressBut("-"))
buttonMinus.grid(row=2, column=3)

buttonMulti = Button(root, text="*", padx=15, pady=15, command= lambda: pressBut("*"))
buttonMulti.grid(row=3, column=3)

buttonDivide = Button(root, text="/", padx=15, pady=15, command= lambda: pressBut("/"))
buttonDivide.grid(row=4, column=3)





root.mainloop()
