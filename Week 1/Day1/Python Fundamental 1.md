
# Python Fundamental 1

## Hello World program

Below is the first example code of printing or print() function



```python
print("Hello World")
print("This is a good example")
print("But what the hell am I writting now?")
print("I'm running out of ideas")
print("F**k ! I'm stucked")
print("Let's just print this")
```

    Hello World
    This is a good example
    But what the hell am I writting now?
    I'm running out of ideas
    F**k ! I'm stucked
    Let's just print this


The print function in Python is a function that outputs to your console window whatever you say you want to print out.
At first blush, it might appear that the print function is rather useless for programming, but it is actually one of the most widely used functions in all of python. The reason for this is that it makes for a great debugging tool.
- If you are familiar with JavaScript, print() is like console.log() in JavaScript

## Comments
Comments are very important in your scripts, you use them to let other people know what you're doing and what the code is doing. This also helps your code to be maintainable.


```python
# print out my lovely hello world program
print("Hello World")
```

    Hello World


## Numbers and Math

You don't need to be a math genius to do programming, if you can count money, you're good to go. Here are some math symbols that you will need to use:
- " +  (plus/add)"
- "-(minus/ substract)"
- "/ (slash/ divide)"
- "*(asterisk/star/multiple)" 
- " % (percent/ modulus)" 
- ">(bigger/greater than)"
- "< (less than)"
- "<= (less than or equal)"
-  ">=(bigger/greater than or equal)"

### Integer and Float numbers ? 
Do you know what are they ?


```python
print("2+2 is", 2+2)
print("2-2 is", 2-2)
print("4/2 is", 4/2)
print("4*2 is", 4*2)
print("5%2 is", 5%2)
print("2 > 3 is", 2>3)
print("2 < 3 is", 2<3)
print("4 >= 4 is", 4>=4)
print("5 <=5 is", 5>=5)
```

    2+2 is 4
    2-2 is 0
    4/2 is 2.0
    4*2 is 8
    5%2 is 1
    2 > 3 is False
    2 < 3 is True
    4 >= 4 is True
    5 <=5 is True


## Exercise:
1. Explain to the person next to you what is going on in the script, why did it show like that?
2. Above each line of code, add a comment to explain what it does
3. Write your own script, using both integer and float numbers and try to use different combination of operation to see the order

## Variables and Names

Variable is nothing more than a name for something. Programmers are not as smart as you think, we need to use variables to make our code read more like English, and also because we have lousy memories. If we don't use a good names for things in the scripts, we'll get lost while trying to read the code again
### Rules
- Variable names are case sensitive (lowercase vs UPPERCASE)
- must start with a letter or an underscore
- can have number but not start with one


```python
apple = 10
orange = 15
basket = apple + orange
bill = basket*10

print("You've bought ",apple," apples")
print("You've also bought", orange, "oranges")
print("Your basket now have {} fruits in it".format(basket))
print("You have to pay %d Dollars" %bill)
```

    You've bought  10  apples
    You've also bought 15 oranges
    Your basket now have 25 fruits in it
    You have to pay 250 Dollars


## Multiple assignment


```python
kiwi, mandarin, tomato, shop, cheaper = (2.5, 3.0, 2, "Lidl", True)
print(kiwi)
print(mandarin)
print(tomato)
print(shop)
print(cheaper)
```

    2.5
    3.0
    2
    Lidl
    True


## Exercise:
1. Again, explain to your partners what is going on in the script, write some comments as well
2. Write you own scripts, use more math, integers and floats
3. Do some research about "format string" in python 3 and test it out

### More exercises

1. Suppose the cover price of a book is ```$24.95```, but bookstores get a ```40% discount```.
Shipping costs ```$3``` for the first copy and ```75``` cents for each additional copy. What is
the total wholesale cost for 60 copies?
2. If I leave my house at 6:52 am and run 1 mile at an easy pace (8m15s per mile), then 3
miles at tempo (7m12s per mile) and 1 mile at an easy pace again, what time do I get
home for breakfast?



```python

```
