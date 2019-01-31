
# Primitive data types
Primitive data types in Python include:
- Boolean (bool)
- Integer (int)
- Float (float)
- String (str)
- None

## Initeger
- Integers are whole number with no decimal numbers, e.g:


```python
x = 1
y= 10
print(f"{x} and {y} are {type(x)} and {type(y)}")
```

    1 and 10 are <class 'int'> and <class 'int'>


## Float
- Float numbers are number that have decimal numbers with it, e.g:


```python
z = 1.3456789
t = 1.00
print(type(z))
print(type(t))
```

    <class 'float'>
    <class 'float'>


## String
- We've used strings quite a lot already so you should have known what a string is. Just like text, if you want to specify a number is a string, use quotation marks around it.  
```
E.g:
"20"
```

## Converting types to types
- int(x) : convert x to integer (x must not be texts)
- float(x) : convert x to float ( x must not be texts)
- str(x) : convert x to string  
E.g: 


```python
x = 1.234
int(x)
```




    1




```python
y = 2
float(y)

```




    2.0




```python
z = 34
str(z)
```




    '34'



## Boolean (bool)
- There is a type of data that has only value True or False. For example: if I say: "Don is the best" the value to be returned will be True, event Definitely True if possible
- To evaluate logics, you will neet to use those terms:  
    - and
    - or
    - not
    - == (equal)
    - != (not equal)
    - \>= ( greater than or equal)
    - \<= ( smaller than or equal)
    - \> (greater)
    - \< (smaller)
    - True
    - False


```python
print ( 1==2)
```

    False



```python
print(3==3)
```

    True



```python
print(not 1==2)
```

    True



```python
print(not 3==3)
```

    False


### not/or/and

| NOT     | TRUE?     | 
|---------|:----------|
| not True    | False     |
| not False    | True     |


| OR     | TRUE?     | 
|---------|:----------|
| True or True|True|
|True or False| True|
|Fale or False| False |
|False or True| True |

| AND     | TRUE?     | 
|---------|:----------|
| True and True|True|
|True and False| False|
|Fale and False| False |
|False and True| False |

# Non-primitive data types
## Lists
As the name said,a list is a container of things that are organized in the order from first to last.  
A list:  
    - is mutable
    - defined by square brackets []
    - items in the list has an index number, start from 0


```python
fruits=["apple", "orange", "pineapple","mandarin"]
type(fruits)
```




    list




```python
fruits[0]
```




    'apple'




```python
fruits[3]
```




    'mandarin'



## [List methods](https://docs.python.org/3/tutorial/datastructures.html)
Some of the often used methods


```python
# Add a new element to the end of the list
list1 = [1,2,3]
list1.append(4)
print(list1)
```

    [1, 2, 3, 4]



```python
# Remove the last element in the list
list1.pop()
print(list1)
```

    [1, 2, 3]



```python
# Insert a new element to a specific position in the list
# The first argument is the position index, the second is the element
list1.insert(0,4)
print(list1)
```

    [4, 1, 2, 3]


## List slicing
You can extract specific element or a group of elements by using [slicing](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/)  



```python
list2 = ['apple','orange','banana','pineapple','mango','avocado','kiwi']
# Use ":" - colon- to separate the starting point and the ending point of the slicing area
# For example, you want to get the first 2 elements in list 2 by:
list2[:2]
# this is the same as list2[0:2]/saying, I want to get the element starting and from and including index number 0
# to 2 but exclude 2, so only 0 and 1
```




    ['apple', 'orange']




```python
print(list2[2:5])
# if you ommit the starting point, python will start from the begining of the list
# if you omit the ending point, python will end at the last item
print(list2[3:])
print(list2[:])
```

    ['banana', 'pineapple', 'mango']
    ['pineapple', 'mango', 'avocado', 'kiwi']
    ['apple', 'orange', 'banana', 'pineapple', 'mango', 'avocado', 'kiwi']



```python
# to reverst the position of elements in the list
list2[::-1]
```




    ['kiwi', 'avocado', 'mango', 'pineapple', 'banana', 'orange', 'apple']




```python
#replace an element in the list
list2[0] = "omena"
print(list2)

# combine two lists
list3 = ["kelemnti","cherry"]
print(list2+list3)
```

    ['omena', 'orange', 'banana', 'pineapple', 'mango', 'avocado', 'kiwi']
    ['omena', 'orange', 'banana', 'pineapple', 'mango', 'avocado', 'kiwi', 'kelemnti', 'cherry']


# Tuples
Tuple is very similar to list, but the key differences are:
- tuple is immutable/ unable to change
- open and close with parenthesis


```python
tuple1 = ("coffe","soft drink","juice")
tuple1[0]
```




    'coffe'




```python
tuple1[0] = "vodka"

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-e8fcbed507c4> in <module>
    ----> 1 tuple1[0] = "vodka"
    

    TypeError: 'tuple' object does not support item assignment



```python
tuple.append("white wine")
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-20-8d60cbba92c1> in <module>
    ----> 1 tuple.append("white wine")
    

    AttributeError: type object 'tuple' has no attribute 'append'


**So when we use tuple and when to use list?**
Use tuple when we want the data in it remain the same and no one will be able to modify it, or else, use lists

### Basic tuple operations
| Python expression | Results | Description |
|-------------------|:--------:|------------:|
|len((1,2,3)) | 3 | Length of tuple |
|(1,2,3) + (4,5,6) | (1,2,3,4,5,6) | concatenation |
| ("Hi")* 4 | ("Hi","Hi","Hi","Hi") | repetition |
| 2 in (1,2,3) | True | Membership |
| for i in (1,2,3): print(i) | 1 2 3 | iteration |

## Dictionaries
Dictionaries is collections of key:value pair.
- Dictionaries open and close by curly brackets {}
- a pair of key and value is separated by a colon (:)
- key must be unique within the dictionary, but the value may not


```python
dict1 = {"name": "John Doe", "age": 30}
```


```python
# access the value using keys
dict1["name"]
```




    'John Doe'




```python
# Adding new key and value
dict1["place"] = "Finland"
```


```python
dict1
```




    {'name': 'John Doe', 'age': 30, 'place': 'Finland'}



# Boolean Exercise:
1. True and True
2. False and False
3. 1 == 1 and 2 == 1
4. "test" == "test"
5. 1 == 1 or 2 != 1
6. True and 1 == 1
7. False and 0 != 0
8. True or 1 == 1
9. "test" == "testing"
10. 1 != 0 and 2 == 1
11. "test" != "testing"
12. "test" == 1
13. not(True and False)
14. not ( 1 == 1 and 0 != 1)
15. not (10 == 1 or 1000 == 1000)
16. not ( 1 != 10) or (3 == 4)
17. not ("testing" == "testing" and "Don" == "Cool Guy")
18. 1 == 1 and (not("testing" == 1 or 1 == 0))
19. "carrot" == "salat" and (not(3 == 4 or 3 == 3))
20. 3 == 3 and (not("testing" == "testing" or "Python" == "fun"))


```python

```
