
# Functions

they do:
 - A function is a block of code which only runs when it is called.
 - You can pass data, known as parameters, into a function.
 - A function can return data as a result.

You can create a function by using the word def in Python.


```python
def example_function():
  print("Hello, this is the example function")

example_function()
```

    Hello, this is the example function



```python
#in this function, num1 and num2 are arguments that you want to process in the function
def add_num(num1, num2):
    result = num1 + num2
    print(f"The result is {result}")
    return result
#pass the argument to the function by passing them to the parenthesis
add_num(2,5)
```

    The result is 7





    7




```python
# you use *args as there are more than one argument but you don't want to write them all down
# or most of the time because you don't know the exact number of arguments that users may insert
def sum_nums(*args):
    arg1, arg2, arg3, arg4 = args
    return arg1 + arg2 +arg3 +arg4

sum_nums(1,2,4,5)
```




    12




```python
def names(*args):
    for arg in args:
        print(f"{arg} is in the list")
names("Jin","Dua", "Mit")
```

    Jin is in the list
    Dua is in the list
    Mit is in the list



```python
names("Lis","Galina","Abby","Hanna", "Rahul", "Alfonso")
```

    Lis is in the list
    Galina is in the list
    Abby is in the list
    Hanna is in the list
    Rahul is in the list
    Alfonso is in the list


## Exercise
- copy the code in this link to your text editor: https://learnpythonthehardway.org/python3/exercise26.txt
- find and fix all the errors to run the file
- use Google, stackoverflow or whatever you can find
- Any feedback about these code ? Good? Bad? Why? How to improve?

### with and without "return":
- Functions that don't have "return" keyword will only do something without returning any value. If we asign it to a variable, the value of the variable will be None
    - For example:
    ```
    def no_return(x,y):
        c = x+y
    
    a = no_return(3,4)
    print(a)
    ```
    This function will return None if 
- We use "return" keyword to tell the function to do something and return an output
    - For example:
    ```
    def with_return(x,y)
        c = x+y
    
    a = with_return(3,5)
    print(a)
    
    >>> 8
    ```


```python
def no_return(x,y):
    c = x+y
```


```python
no_return(1,2)
```


```python
x = no_return(1,2)
print(x)
```

    None



```python
def with_return(x,y):
    c = x+y
    return c
b = with_return(3,5)
print(b)
```

    8



```python

```
