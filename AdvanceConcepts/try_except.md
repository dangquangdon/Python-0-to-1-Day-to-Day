# Try/Except block for Error handling

## Why and How?

For example when we are itterating through this list and try to convert all numbers to integers

```python
list1 = [1.2, 3, "one more", 4.5]
for each in list1:
    element = int(each)
    print(element)
```

Python will throw you an error and stop the program

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: 'one more'
```

Now if we put them into `try/except` block

```python
list1 = [1.2, 3, "one more", 4.5]
for each in list1:
    try:
        element = int(each)
    except Exception:
        print("This element is not convertable")
    print(element)
```

When we run this code, even if we have some errors, the code will throw the error but will keep continue working.

- If we want to be more specific, in the `except` statement, we specify what type of error we want to catch and print a specific message for it. For example

  ```python
  ...
  except ValueError:
      print("Wrong type of value")
  except Exception:
      print("Something went wrong")
  ```

or

```python
...
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
```

So we can catch multiple errors as we anticipate, however, keep in mind that we should put the `Exception` to the end so that python will try to look for how to react to a specific errors first, before throwing some more general error.

### Else & Finally

`else` block will be excuted if the `try` block does not raise any `Exception`. Or in other word, if the `try` block runs successfully, the `else` block will be excuted, if not, `else` will not be called. For example

```python
list1 = [1.2, 3, "one more", 4.5]
for each in list1:
    try:
        element = int(each)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(element)
```

Ofcourse we could actually put our `print()` function right inside the `try` block, however, if there is a bigger and longer block of code, the errors might not be from the `element`, but from someother lines in that block instead. If so, we won't be able to catch and handle the errors as specifically as we want, unless we have to nest another block of `try/except` in it.

Lastly, `finally` block:

```python
list1 = [1.2, 3, "one more", 4.5]
for each in list1:
    try:
        element = int(each)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(element)
    finally:
        print("It's done finally")
```

`finally` block will run regardless of what's happening and finish off the code.
