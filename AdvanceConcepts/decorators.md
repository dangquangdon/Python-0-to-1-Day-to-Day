# Decorators

## First-class function

First-class function is not a type of function, but instead, it is a characteristic of a programming language.

So a programming language that has first-class function characteristic, should treat function as all other first-class data/object. Which means, we can assign variable name for a function, pass it in another function as an argument, return it in another function.

## Closure

Closure will take the advantages of first-class function, it returns an inner function that remember and has the access to variables in the local scope in which it was created. For example

```python
def outer_function():
    # local variable
    name = "Don"

    def sayHi():
        print("Hi," + name)
    return sayHi()

outer_function()
>>> Hi, Don
```

In this example, when `outer_function` is called, it will return `sayHi()` which will execute the `sayHi` inner function immediately because we put `()` after `sayHi`

Let's try to remove `()` in `sayHi`

```python
def outer_function():
    # local variable
    name = "Don"

    def sayHi():
        print("Hi," + name)
    return sayHi

outer_function()
>>> <function outer_function.<locals>.sayHi at ...>
```

In this case, the `outer_function` only return `sayHi` without executing it. If we assign it to a variable

```
func_1 = outer_function()

func_1()
>>> Hi, Don
```

So we've stored the return of `outer_function` to a variable call `func_1`, and now `func_1` becomes a function, and it can call the variable from `outer_function` scope, which is `name`, and return `Hi, Don`

### With argument(s)

The same example, but we will change it a bit, instead of giving the value to `name`, we will pass it in as an argument.

```python
def outer_function(name):

    def sayHi():
        print("Hi," + name)
    return sayHi

func_1 = outer_function("Daniel")
func_1()
>>> Hi, Daniel

func_2 = outer_function("Eva")
func_2()
>>> Hi, Eva
```

## Decorators

Decorator is a function that take a function as argument and return an other function.
The structure looks like this

```python
def decorator_function(a_function):
    def wrapper_function():
        return a_function()
    return wrapper_function
```

let's create a simple test function, and pass it in `decorator_function`

```python
def sayHi():
    print("Hi there!")

decorated = decorator_function(sayHi)

decorated()
>>> Hi there!
```

So what happens is,

- we've passed `sayHi` to the `decorator_function`
- and it will return a `wrapper_function` waiting to be called.
- We've then assigned it to `decorated` variable, that makes `decorated` become a function
- Then we've called `decorated` which would strigger `wrapper_function` and then strigger `sayHi`

The syntax `decorator_function(sayHi)` we've just done is actually the original way. However, we will see in practise something like this and they are the same.

```python
@decorator_function
def sayHi():
    print("Hi there!")
```

So, what exactly we could do with a decorator. Now if we modify the `wrapper_function` a bit

```python
...
    def wrapper_function():
        print("hello, it is me you're looking for")
        return a_function()
```

Now, when we use `@deocrator` syntax

```python
@decorator_function
def sayHi():
    print("Hi there!")

sayHi()
>>> "hello, it is me you're looking for"
>>> "Hi there!"
```

So we basically have just add 'new feature' to `sayHi` without putting our hands to the original code of `sayHi`. And that's what decorators do.

In short, we use decorators to add new features or functionalities to a function without modifying its code lines.

**However**

What if `sayHi` takes 2 or 3 or even more parameters. For example, we wnat `sayHi` function to behave like this

```python
def sayHi(name, title):
    print("Hi there, {} - {}".format(name, title))

sayHi("Daniel", "The Slayer")
>>> "Hi there, Daniel - The Slayer"
```

So when we put the decorator to this `sayHi` function, python will throw and error. Try to findout why?

The solution for this is to pass positinal arguemens and keword arguments to `wrapper_function`

```python
...
    def wrapper_function(*args, **kwargs):
        ...
        return a_function(*args, **kwargs)
```

### Class decorator

We can also create a class and use it as decorator, and it will do the same thing as a function decorator do. However, we will have to use some classes' syntax to do that.

```python
class decorator_class(object):
    def __init__(self, a_function):
        self.a_function = a_function

    def __call__(self, *args, **kwargs):
        print("hello, it is me you're looking for")
        return self.a_function(*args, **kwargs)
```

In a class decorator, the `__call__` method is acting like a `wrapper_function` in function decorator. The difference is that, in function decorator, we can name `wrapper_function` anything we want, however, in class decorator, the `__call__` is a must.

Whether to use class decorator or function decorator is personal preference. You can use whatever way you feel comfortable with or you feel more suitable.

# Example of practical use-case

For example, we have a function, and we want to use `logging` library to monitor the use of our function

```python

def logger_file(func):
    import logging

    filename = "{}.log".format(func.__name__)

    logging.basicConfig(filename=filename,
                        level=logging.INFO)

    def wrapper(*args, **kwargs):
        info = "Ran with args: {}, and kwargs: {}".format(args, kwargs)
        logging.info(info)
        return func(*args, **kwargs)

    return wrapper

@logger_file
def sayHi(name, title):
    print("Hi there, {} - {}".format(name, title))

sayHi("Daniel", "The King")
```

Excecute the script and notice the changes in your working directory. Do you have some idea of what `logging` does now?

Let's try with an other decorator

```python
def timer(func):
    import time

    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()

        filename = func.__name__
        runtime = t2 - t1

        print("{} ran in {} sec".format(filename, runtime))

        return result

    return wrapper_func

@timer
def sayHi(name, title):
    print("Hi there, {} - {}".format(name, title))

```

What would happen if we want to apply both of these decorators to `sayHi`. If we try this:

```python
@timer
@logger_file
def sayHi(name, title):
    print("Hi there, {} - {}".format(name, title))
```

In this case:

- When `sayHi` is executed, `@logger_file` will do its job, which will add the feature of logging out a logfile to store the history of arguments that `sayHi` use.
- Then `@timer` will do its job, to estimate the running time of the function that is passed in. But this time, the function that is passed in is not `sayHi` anymore, it is actually the `wrapper` of `logger_file`.
- And vice versa, if we put `@logger_file` first, and `@timer` second. The two actions will be vice versa, and they are both not applying for the same `sayHi` function.

To solve this, we will need an extra help from a standard library of python called `functools`

```python
from functools import wraps

def logger_file(func):
    ...
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...



def timer(func):
    ...
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        ...
```
