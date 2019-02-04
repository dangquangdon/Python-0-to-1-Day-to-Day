
# Parameters, Unpacking, Read and Write Files

We will learn more input method you can use to pass vairables to a script


```python
from sys import argv
```

[sys module](https://docs.python.org/2/library/sys.html) provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
- ```argv```  
The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.

Example code:

```
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
```

To run this code, you have to pass in to your command line 3 other aguement after the script name.  
If normally you run the script as ``` python script.py ```, now you run ``` python script.py first second third ```  
The ``` script.py ``` will be execute, and ``` first```, ```second```, ```third```, will be consider as variable and import into the script, by default, they will be string

## Prompting (input()) and Passing(argv)
The different has to do with where the user is required to give input. If they give your script inputs on the command line, then use ``` argv ```. If you want them to input using the keyboard while the script is running, use ```input()```

Try this code, explain what's going on to your partner and also write it down as comments:
```
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.
And you have a {computer} computer.
""")
```

### Exercise
- Download or Clone this https://github.com/iamjawa/zork-py/blob/master/zork.py
- Run the file and play the game
- Read the code, try to change the prompt variable to something else
- add or replace some prompt variable with arguement variable ``` argv``` like you did in the sample code above

## Read and Write files
- first, you have to create a text file (txt file) and write something you want in it, anything, for example  
```
This is stuff I typed into a file
It is really cool stuff
Lots and lots of fun to have in here
```

- now type this sample code and try it out:  

```
from sys import argv


script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
```

[open()](https://docs.python.org/3/library/functions.html#open) is a built-in function of python. It is used to open a file and return it as a file object.  
Syntax  
``` open(file, mode) ```  

Including a mode argument is optional because a default value of ‘r’ will be assumed if it is omitted. The ‘r’ value stands for read mode, which is just one of many.  

Some often used modes are:  

- ‘r’ – Read mode which is used when the file is only being read 
- ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
- ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
- ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file


```read()``` is a method that is used to read the file that we've just opened.  
By default ```read()``` method return the whole text, but we can also define how many characters we want it to show

#### Extra
```readline()```  
- if you want to return only one line or one specific line in the file. For example  
```readline()``` - return the first line  
``` readline(5)``` - return the fifth line

```close()``` - to close the file  
```write('some stuff')``` - writes "some stuff" into the file

### More sample codes
```
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file.Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")


print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
```

### Exercise
- Explain to your partner what's going on in the script and write it down as comments
- There are too much of repeatation in this file, use string format and escape characters to re-write ```line1```, ```line2```, ```line3``` with just one ```target.write()``` command.

#### Extra
- Copy content of one file to another
- try this, and repeat the first exercise  


```
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
```

**Note:**
- When using **pen()** to open a file to do something with it, we have to use **close()** to close down the file and save changes
For example:  
```
file = open("sample.txt","w")
file.write("Write something !")
file.close()
```

**Other way of working with files is to use Context Manager - 'WITH statement'**  
**And this way is more RECOMMENDED**
```
with open("sample.txt", "w") as f:
    f.write("Write something !")
```
- this way, we no longer need close() function
- Even if there's an error, the file still get closed properly
- There are so much more useful stuff with WITH Statement, not just working with files, you will learn more later on



```python

```
