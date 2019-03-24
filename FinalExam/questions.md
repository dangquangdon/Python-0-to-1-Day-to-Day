# Code Chanllenges

Please complete these challenges below. Write separate scripts for each challenge.

If you want to test your result, feel free to write an unit test script of your own, or you can just simply test it manually by using another argument for your function.

**To asnwer:**

- Copy the Starter Code to your script and write your answer to the are that said #YOUR CODE GOES HERE.

- Feel free to alter the `return` accodingly as well as deleting the `pass`

**To submit this:**

- Create a github repo in your own github account, and push all of the scripts there.

- Write a README.md file to let other people know that these are your answers for the code challenge. Make it as pretty as you can

### 1. Palindrome - easy

A _palindrome_ is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, `is_palindrome("Deleveled")` should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

**Starter Code**

```python
def is_palindrome(word):
    # YOUR CODE GOES HERE
    return None

print(is_palindrome('Deleveled'))
# This should print True

```

### 2. Merge Names - easy

Implement the unique_names method. When passed two arrays of names, it will return an array containing the names that appear in either or both arrays. The returned array should have no duplicates.

For example, calling

`unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])`

should return an array containing Ava, Emma, Olivia, and Sophia in any order.

**Starter Code**

```python
def unique_names(names1, names2):
    # YOUR CODE GOES HERE

    return None

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
# should print Ava, Emma, Olivia, Sophia
```

### 3. Ice Cream Machine - medium

Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. If there are no ingredients or toppings, the method should return an empty list.

For example,

`IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()`

should return

`[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]`.

**Starter Code**

```python
class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        # YOUR CODE GOES HERE

        pass

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())
#should print
# [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())
# this should print
#[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce'], ['vanilla','orange'], ['chocolate','orange']]
```

### 4. Pipeline - hard

As part of a data processing pipeline, complete the implementation of the pipeline method:

- The method should accept a variable number of functions, and it should return a new function that accepts one parameter arg.

- The returned function should call the first function in the pipeline with the parameter arg, and call the second function with the result of the first function.

- The returned function should continue calling each function in the pipeline in order, following the same pattern, and return the value from the last function.

For example, pipeline(lambda x: x \* 3, lambda x: x + 1, lambda x: x / 2) then calling the returned function with 3 should return 5.0.

**Starter Code**

```python
def pipeline(*funcs):
    def helper(arg):
        # YOUR CODE GOES HERE
        pass
    return helper

fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))

#should print 5.0
```

### 5. File Owners - medium

Implement a group_by_owners function that:

- Accepts a dictionary containing the file owner name for each file name.

- Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary:

```
{
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
```

the group_by_owners function should return

```
{
    'Randy': ['Input.txt', 'Output.txt'],
    'Stan': ['Code.py']
}
```

**Starter Code**

```python
def group_by_owners(files):
    # YOUR CODE GOES HERE

    return None

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
```

### 6. Song - hard

A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist. Otherwise, the playlist will end with the last song which points to None.

Implement a function is_repeating_playlist that returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.

```python
first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")

first.next_song(second);
second.next_song(third);
third.next_song(first)

print(first.is_repeating_playlist())
```

should return True

**Starter Code**

```python
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
         # YOUR CODE GOES HERE

        return None

first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")

first.next_song(second);
second.next_song(third);
third.next_song(first)

print(first.is_repeating_playlist())
# This should return True

```
