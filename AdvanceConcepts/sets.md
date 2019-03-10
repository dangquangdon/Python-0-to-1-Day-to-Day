# Sets

## What is a set ?

Set is actual one of the data types that Python offers, the same as List, Dictionary or Tupple, however, set is less mentioned and seens than the others. In fact, set is very useful for some certain types of proplem.

A set is like a list, however, it removes all duplicate values, so set is very useful in finding the intersections of multiple lists, or in comparison multiple lists, etc.

This is how a set looks like

```python
set1 = {1,2,3,4,5,6}
```

A set starts and ends by a pair of `{}`, seems like a dictionary, but the elements inside the `{}` are like elements in a list.

However, when we want to create an empty set, we **cannot** start like this:

```python
set1 = {}
```

because, python will understand that we want to create an empty dictionary now. Instead, we will use this syntax:

```python
set1 = set()
```

When we want to create a set, we have to pass the elements in the set to `set()` as a list inside the `()`. Like this

```python
set1 = set([1,2,3,4])
```

### Add new values to a set

**Add a single value**
To add a single value to a set, we use `add` function.

```python
set1 = {1,2,3,4,5}
set1.add(6)
```

**Add multiple values**
To add multiple values, we use `update` function, and pass in those values as a list to `update` function.

```python
set1 = {1,2,3,4,5}
set1.update([6,7,8])
```

We can also use `update` with other set as well

```python
set1 = {1,2,3,4,5}
set2 = {7,8,9}

set1.update([6,7,8], set2)
```

In this example, `set1` will update and add new values from the list `[6,7,8]` and also from set `set2`. However, it will remove the duplicate values from these two inputs.

**Remove a value**

There are two ways to remove a single value from a set

- `remove` function:
  ```python
  set1 = {1,2,3,4,5}
  set1.remove(5)
  ```
- `discard` function:
  ```python
  set1 = {1,2,3,4,5}
  set1.discard(5)
  ```

The difference between `remove` and `discard` is that, if we try to remove a value that does not exist in the set, `remove` will stop the program and throw and error, while `discard` will not throw any error and still return the state of the original set.

**Get the intersection**

To get the intersection of multiple sets, use can simply use `intersection` function. It will return the common elements that multiple sets can have.

```python
set1 = {1,2,3}
set2 = {3,4,5}

intersec1 = set1.intersection(set2)
intersec2 = set2.intersection(set1)
print(intersec1)
>>> {3}
print(intersec2)
>>> {3}
```

More than two:

```python
set1 = {1,2,3}
set2 = {3,4,5}
set3 = {4,5,6}
set4 = {3,5,7}
intersec1 = set1.intersection(set2, set3)
intersec2 = set1.intersection(set2, set4)
print(intersec1)
>>> set()
print(intersec2)
>>> {3}
```

**Get the differences between multiple sets**

To get the differences, we use `difference` function.

```python
set1 = {1,2,3}
set2 = {3,4,5}
set3 = {4,5,6}
set4 = {3,5,7}
diff1 = set1.difference(set2)
print(diff1)
>>> {1,2}
diff2 = set2.difference(set1)
>>> {4,5}
diff3 = set2.difference(set1, set3)
>>> set()
diff4 = set2.difference(set1, set3, set4)
>>> set()
diff5 = set1.difference(set2, set3, set4)
>>> {1,2}
```

**Symmetric difference**
In the example above, when we try to find the difference between `set1` and `set2`

```python
diff1 = set1.difference(set2)
print(diff1)
>>> {1,2}
diff2 = set2.difference(set1)
>>> {4,5}
```

If we use `set1` to compare with `set2`, we got only the elements that is from `set1`, and vice versa to get the elements from `set2`.

To get both differences from `set1` and `set2` together, we use `symmetric_difference` function

```python
...
set1.symmetric_difference(set2)
>>> {1,2,4,5}
set2.symmetric_difference(set1)
>>> {1,2,4,5}
```

`symmetric_difference` will return the differences element from both `set1` and `set2` regardless of which one is calling.
