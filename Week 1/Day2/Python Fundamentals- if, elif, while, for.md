
# If statement

Flow Diagram
![if_else_statement.jpg](attachment:if_else_statement.jpg)



```python
guess = int(input("Choose a number between 0 and 5: "))
answer = 3
if guess == answer:
    print("Super ! How did you do that ?????")
else:
    print("Wrong ! Ehhhhhhh !")
```

    Choose a number between 0 and 5: 1
    Wrong ! Ehhhhhhh !


# elif (else if)
**elif allows us to check multiple conditions and excecute different blocks of codes accordingly**




```python
guess = int(input("Choose a number between 0 and 5: "))
answer = 3
if guess == 1:
    print("No no, higher !")
elif guess == 2:
    print("Almost correct !")
elif guess == 3:
    print("Yessss !!!!")
else:
    print("Wrong ! Ehhhhhhh !")
```

    Choose a number between 0 and 5: 3
    Yessss !!!!


# Loops
**In general, a loop consists of one or more blocks of code that keeps running as long as the checking condition is still valid/True**
![loop_architecture.jpg](attachment:loop_architecture.jpg)

## While loop
A while loop statement repeatedly executes a target statement as long as a given condition is true.
- Syntax
    ```
    while condition:
        do something
    ```


```python
count = 0
while count < 5:
    print(count)
    count += 1
print("Done!")
```

    0
    1
    2
    3
    4
    Done!


## for loop
It has the ability to iterate over the items of any sequence, such as a list or a string.
- Syntax
    ```
    for a in something:
        do something with a
    ```


```python
hi = "Hello World!"
for ch in hi:
    print(ch)
```

    H
    e
    l
    l
    o
     
    W
    o
    r
    l
    d
    !



```python
dict1 = {"key1": 1, "key2": 2}
for i in dict1:
    print(i)
```

    key1
    key2



```python
list1 = [1,2,3,4,5]
for i in list1:
    print(i)
```

    1
    2
    3
    4
    5



```python

```
