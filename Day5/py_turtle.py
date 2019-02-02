# Remember to practice using virtualenv
# put this script in a folder of its own, and create virtual environment for it
# activate the virtual environment and play with the script


import turtle
from random import randint

# Change the color and shape value to see the different
# Let's google the other values of them

abby = turtle.Turtle()
abby.color('red')
abby.shape('turtle')

abby.penup()
abby.goto(-200, 200)    # Change the values to see the different as well
abby.pendown

lis = turtle.Turtle()
lis.color('blue')
lis.shape('turtle')

lis.penup()
lis.goto(-200, 100)
lis.pendown

galina = turtle.Turtle()
galina.color('orange')
galina.shape('turtle')

galina.penup()
galina.goto(-200, 0)
galina.pendown

for move in range(200):
    # Change randint() value to see the different
    abby.forward(randint(1, 5))
    lis.forward(randint(1, 5))
    galina.forward(randint(1, 5))


turtle.done()
