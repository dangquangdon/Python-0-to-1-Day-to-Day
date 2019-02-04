
# Python Fundamental 2
## Strings and Text

- A string is usually a bit of text you want to display to someone or 'export' out of the program.
- Strings in python are surrounded by either single or double quatation marks
- String can contain any number of variables that are in your Python script
- You have seen different ways of formating a string in the previous topic

### More practice


```python
members = 22
str1 = f"There are {members} people in The Shortcut Team"

handsome = "handsome"
are_not = "aren't"

str2 = f"Those who are {handsome} and those who {are_not}"

print(str1)
print(str2)

print(f"I will say again {str1}")
print("I also said {}".format(str2))

funny = False

joke_evaluation = "Isn't it so funny? {}"
print(joke_evaluation.format(funny))
```

    There are 22 people in The Shortcut Team
    Those who are handsome and those who aren't
    I will say again There are 22 people in The Shortcut Team
    I also said Those who are handsome and those who aren't
    Isn't it so funny? False


## Escape Sequences

This is all the escape sequences Python supports. You may not use many of these, but memorize their format and what they do anyway. Try them out in some strings to see if you can make them work


| Escape | What it does |  
|-------:|-------------:|
|\\\ | Backslash (\\) |
|\\' | Single-quote (\') |
|\\" | Double-quote (\") |
|\\a | ASC II bell (BEL) |
|\\b | ASC II Backspace (BS) |
|\\f | ASC II formfeed (FF) |
|\\n | ASC II linefeed (LF) |
|\\N{name} | Character named name in the Unicode database (Unicode only) |
|\\r | Carriage Return (CR) |
|\\t | Horizontal Tab (TAB) |
|\\uxxxx | Character with 16-bit hex value xxxx |
|\\Uxxxxxxxx| Character with 32-bit hex value xxxxxxxx |
|\\v | ASC II vertical tab (VT) |
|\\ooo | Character with octal value ooo|
|\\xhh | Chracter with hex value hh|

## Input
Simply, You can use input() to get input value from keyboard and assign it to a variable.



```python
age = input("How old are you? ")
```

    How old are you? 3



```python
age
```




    '3'



### Exercise
- Use Google to findout more about input()

## String metheds
Python has many methods that a string can call to perfom tasks. For more detail, check [w3school Python](https://www.w3schools.com/python/python_ref_string.asp)  
*** Do not confuse with [string module](https://docs.python.org/3/library/string.html)


```python
example = "hello beautiful !"
```


```python
#Converts the first character to upper case
example.capitalize()
```




    'Hello beautiful !'




```python
#Returns the number of times a specified value occurs in a string
example.count('l')
```




    3




```python
#Splits the string at the specified separator, and returns a list
example.split(' ')
```




    ['hello', 'beautiful', '!']




```python
#Returns true if the string starts with the specified value
example.startswith('H')
```




    False




```python
#Converts the first character of each word to upper case
example.title()
```




    'Hello Beautiful !'




```python
#Indexing
example[0]
```




    'h'




```python
#Slicing
example[0:6]
```




    'hello '




```python

```
