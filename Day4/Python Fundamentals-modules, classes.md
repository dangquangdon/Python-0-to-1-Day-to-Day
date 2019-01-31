
# Modules, Classes and Objects

## Modules
- It is a Python file/script with some functions or variables in it
- You can import that file in another script
- And you can access/use the functions or variables in the script with the dot operator

```
# Create a file test_module.py
# In test_module.py

def apple():
    print("this is an apple")

secret = "this is a secret"
```

```
# Create a second import_example.py
# In import_example.py

import test_module

test_module.apple()
print(test_module.secret)
```


## Classes

A class is a way to take a group of functions and data, and put them together  in a container so that you can access them and reuse them from anywhere

- Create a class with ```class``` keyword. This is python reserved keyword used only for creating classes
- Syntax:  
```
class Human:
    """
        Docstring to explain what is this, what it does
    """
    def __init__(self, name, age):
        self.name = name,
        self.age = age
     
     def who(self):
         print(f"This is {self.name}, {self.age} years old")
```

### Instances
- Class is a blueprint for creating instances
- Each unique instance created by using a class, will be an instance of that class


```python
class PythonProgrammer:
    pass
    

programmer_1 = PythonProgrammer()
programmer_2 = PythonProgrammer()
print(programmer_1)
print(programmer_2)
```

    <__main__.PythonProgrammer object at 0x10f87d630>
    <__main__.PythonProgrammer object at 0x10f87d390>


#### Instance's Variables

The PythonProgrammer class above doesn't have anything in it, so do instances. Therefore, we have to add variables to instances. We could add variables in Class level -> apply for all instances of that class, or we add variables in instance level -> apply for only that instance.
- Let's try


```python
programmer_1.first_name = "John"
programmer_1.last_name = "Doe"
programmer_1.email = "john.doe@python.com"

programmer_2.first_name = "Jane"
programmer_2.last_name = "Doer"
programmer_2.email = "jane.doer@python.com"

print(programmer_1.email)
print(programmer_2.email)

```

    john.doe@python.com
    jane.doer@python.com


- So you can create different variables for each instance, however, it takes a lot of time and codes to do this manually, also, we don't get the benefit of using class here
- To set it up automatically, we use __init__() method in the PythonProgrammer class


```python
class PythonProgrammer:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"
        
# When we create a method within a class, they receive the instance as the first argument automatically.
# Basically you can call it anything you want, but by convention and for a best practise, we call it self
# After self, you can specify what other arguments that we need
```


```python
pr_1 = PythonProgrammer("John","Doe")
pr_2 = PythonProgrammer("Janet","Doer")
```


```python
print(pr_1.email)
print(pr_2.email)
```

    John.Doe@python.com
    Janet.Doer@python.com



```python
print(pr_1.first_name)
print(pr_2.last_name)
```

    John
    Doer


#### Class Variables
- pr_1 and pr_2 are instances of the PythonProgrammer class, and those variables that created with the self keyword are instance's variables
- **Class variables are variables that share among all instances of that class. While instance's variables can be different and unique like the first_name, last_name, class variables are the same for all instance**
- In this example, let's assume that our programmers have one thing in common, they all know Python and use Python only

**First of all, let's hard code it in a method and compare**


```python
class PythonProgrammer:
    """DocString"""
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"
    
    def speak(self):
        print(f"{self.first_name} speak Python")
```


```python
pr_1 = PythonProgrammer("John","Doe")
pr_2 = PythonProgrammer("Janet","Doer")
pr_3 = PythonProgrammer("Jimmy", "Joe")
```


```python
pr_3.speak()
```

    Jimmy speak Python



```python
pr_1.speak()
```

    John speak Python


**In this case, we are able to see what language they are "speaking", however, if we just want to access only the language they're speaking without calling a method, or we want to change it into something else, for example JavaScript, we will have to go to the code and change it within the source code**

Let's create a class variable


```python
class PythonProgrammer:
    """DocString"""
    
    language = "Python"
    
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"
    
    def speak(self):
        print(f"{self.first_name} speak {self.language}")

pr_1 = PythonProgrammer("John","Doe")
pr_2 = PythonProgrammer("Janet","Doer")
pr_3 = PythonProgrammer("Jimmy", "Joe")

# Important: Once we create a class variable, we can access it through the class itself or through instance.
# It means, instead of putting self.language, we can also put PythonProgrammer.language
# However, if we put only language without the self or class name, it will throw an error
```


```python
pr_1.speak()
```

    John speak Python



```python
# Under the hood, it will go like this
# When we call a variable from an instance, first python will check if the instance has that variable
# If not => check the class that the instance belongs to or inherit from

print(pr_1.language)
print(pr_2.language)
print(pr_3.language)
print(PythonProgrammer.language)
```

    Python
    Python
    Python
    Python



```python
# In the code above, we can access the language variable using pr_1.language.
# Now when we print out all variables of pr_1, we won't see the language variable anymore, as explained above,
# Python then goes to the class to find the variable
print(pr_1.__dict__)
print()
print(PythonProgrammer.__dict__)
```

    {'first_name': 'John', 'last_name': 'Doe', 'email': 'John.Doe@python.com'}
    
    {'__module__': '__main__', '__doc__': 'DocString', 'language': 'Python', '__init__': <function PythonProgrammer.__init__ at 0x10f869488>, 'speak': <function PythonProgrammer.speak at 0x10f869ea0>, '__dict__': <attribute '__dict__' of 'PythonProgrammer' objects>, '__weakref__': <attribute '__weakref__' of 'PythonProgrammer' objects>}



```python
# If we do this, new instance variable will be created just for pr_1
pr_1.salary = 10000
print(pr_1.__dict__)
print()
print(pr_2.__dict__)
```

    {'first_name': 'John', 'last_name': 'Doe', 'email': 'John.Doe@python.com', 'salary': 10000, 'language': 'JavaScript'}
    
    {'first_name': 'Janet', 'last_name': 'Doer', 'email': 'Janet.Doer@python.com'}



```python
# If we change the variable language from Python to JavaScript in pr_1
pr_1.language = "JavaScript"
print(pr_1.language)
print(pr_1.__dict__)
print(pr_2.language)
print(PythonProgrammer.language)
```

    JavaScript
    {'first_name': 'John', 'last_name': 'Doe', 'email': 'John.Doe@python.com', 'salary': 10000, 'language': 'JavaScript'}
    JavaScript
    JavaScript



```python
# If we change the variable language from Python to Ruby in the class
PythonProgrammer.language = "Ruby"

print(pr_2.language)
print(pr_3.language)
print(PythonProgrammer.language)
print(pr_1.language)
```

    Ruby
    Ruby
    Ruby
    JavaScript


#### Excerise

**The same class as we practised, with a small modification** 


```python
class PythonProgrammer2:
    """DocString"""
    
    language = "Python"
    number_of_developers = 0
    
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"
        
        PythonProgrammer2.number_of_developers += 1
    
    def speak(self):
        print(f"{self.first_name} speak {self.language}")
```

1. Create 3 new instances from this Class
2. Check out the number_of_developers variable and explain what's going on


### Methods
- There are 3 types of methods:  
    - Regular methods
    - Static methods
    - Class methods
**Regular methods**
- We have tried using and creating regular methods in the above examples. Basically, **regular methods will automatically take the instance as a parameter/argument - ```self``` keword**


**Class methods**
- Similar to ```Regular methods``` but instead of taking instances as arguments, class methods take the class itself as argument.
- To turn a regular method into a class method, we just need to add a decorator ```@classmethod``` above the method
- And instead of ```self``` keyword, we use ```cls``` keword, stands for "class", but as mentioned, ```class``` keword is reserved only for creating classes, so we have to use something else


```python
class PythonProgrammer3:
    """DocString"""
    
    language = "Python"
    number_of_developers = 0
    
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"
        
        PythonProgrammer3.number_of_developers += 1
    
    def speak(self):
        print(f"{self.first_name} speak {self.language}")
    
    @classmethod
    def set_language(cls, lang):
        cls.language = lang
```


```python
py_dev_1 = PythonProgrammer3("Clark", "Kent")
py_dev_2 = PythonProgrammer3("Peter","Parker")

print(py_dev_1.language)
print(py_dev_1.language)
print(PythonProgrammer3.language)
```

    Python
    Python
    Python



```python
PythonProgrammer3.set_language("Java")

print(py_dev_1.language)
print(py_dev_1.language)
print(PythonProgrammer3.language)

# When we use class method, we are working with class and variables are classes variables
```

    Java
    Java
    Java



```python
py_dev_1.set_language("C++")

print(py_dev_1.language)
print(py_dev_1.language)
print(PythonProgrammer3.language)

# You can access the class methods and change class variable through instances
```

    C++
    C++
    C++



```python
# Image we have a list of name in this format "Firstname-Lastname"
# We have to use string method split() to split the names and create instances
name_string = "Bruce-Lee"
first_name, last_name = name_string.split('-') # Remember this ?
py_dev_bl = PythonProgrammer3(first_name, last_name)
print(py_dev_bl.__dict__)
```

    {'first_name': 'Bruce', 'last_name': 'Lee', 'email': 'Bruce.Lee@python.com'}



```python
# Instead of doing the above, we can use class method 
# Can you explain the flow here ?

class PythonProgrammer3:
    """DocString"""
    
    language = "Python"
    number_of_developers = 0
    
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"
        
        PythonProgrammer3.number_of_developers += 1
    
    def speak(self):
        print(f"{self.first_name} speak {self.language}")
    
    @classmethod
    def set_language(cls, lang):
        cls.language = lang
        
    @classmethod
    def from_string(cls, string):
        first_name, last_name = string.split('-')
        return cls(first_name, last_name)
    
```


```python
py_dev_str = PythonProgrammer3.from_string("Doctor-Strange")
```


```python
print(py_dev_str.__dict__)
```

    {'first_name': 'Doctor', 'last_name': 'Strange', 'email': 'Doctor.Strange@python.com'}


**static methods**
- Regular method automatically take instances as argument - ```self```
- Class method automatically take the class itself as argument - ```cls```
- Static methods does not take ```self``` or ```cls``` as argument automatically
- And we use ```@staticmethod``` decorator to specify that this is a static method  

We add static methods into a class might be because it has some logical connection with the class


```python
# Instead of doing the above, we can use class method 
# Can you explain the flow here ?

class PythonProgrammer3:
    """DocString"""
    
    language = "Python"
    number_of_developers = 0
    
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        self.email = f"{firstname}.{lastname}@python.com"
        
        PythonProgrammer3.number_of_developers += 1
    
    def speak(self):
        print(f"{self.first_name} speak {self.language}")
    
    @classmethod
    def set_language(cls, lang):
        cls.language = lang
        
    @classmethod
    def from_string(cls, string):
        first_name, last_name = string.split('-')
        return cls(first_name, last_name)
    
    @staticmethod
    def isworking(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return True
        
        return False

# in this example, we want to have a method to check if these developers are working only in the weekend
# This has a bit connection with the class but it doesnt need to access the instance or class variables

py_dev_x = PythonProgrammer3.from_string("Jacky-Chan")
print(py_dev_x.__dict__)
```

    {'first_name': 'Jacky', 'last_name': 'Chan', 'email': 'Jacky.Chan@python.com'}



```python
import datetime
today = datetime.datetime.now().date()
print(today)
py_dev_x.isworking(today)
```

    2019-01-26





    True




```python
py_dev_x.isworking(today)
```




    True



### Inheritance

We can create a new class that has all of the attributes from other class.
```
class JuniorDeveloper(PythonProgrammer3):
    pass
```
in this example, the class JuniorDeveloper is call a subclass of PythonProgrammer3. And by doing this, JuniorDeveloper will inherit all of the attributes that PythonProgrammer3 has


```python
class JuniorDeveloper(PythonProgrammer3):
    pass

print(JuniorDeveloper)
```

    <class '__main__.JuniorDeveloper'>



```python
ju_dev = JuniorDeveloper("Jimmy","Yoh")
```


```python
ju_dev.__dict__
```




    {'first_name': 'Jimmy', 'last_name': 'Yoh', 'email': 'Jimmy.Yoh@python.com'}




```python
help(ju_dev)
```

    Help on JuniorDeveloper in module __main__ object:
    
    class JuniorDeveloper(PythonProgrammer3)
     |  DocString
     |  
     |  Method resolution order:
     |      JuniorDeveloper
     |      PythonProgrammer3
     |      builtins.object
     |  
     |  Methods inherited from PythonProgrammer3:
     |  
     |  __init__(self, firstname, lastname)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  speak(self)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from PythonProgrammer3:
     |  
     |  from_string(string) from builtins.type
     |  
     |  set_language(lang) from builtins.type
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from PythonProgrammer3:
     |  
     |  isworking(date)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from PythonProgrammer3:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonProgrammer3:
     |  
     |  language = 'Python'
     |  
     |  number_of_developers = 2
    



```python
print(ju_dev.language)
PythonProgrammer3.set_language("Golang")
print(PythonProgrammer3.language)
```

    Python
    Golang



```python
ju_dev.set_language("Ruby")
```


```python
ju_dev.language
```




    'Ruby'



**Subclasses inherit from the parent classes, however, we can modify the subclasses themselves without modifying parent classes**
```
class JuniorDeveloper(PythonProgrammer3):
    def __init__(self, first, last, salary):
        super().__init__(first,last)
        self.salary = salary
```

What is happening here is that:
- We redefine how we want to instantiate (create) new instances of JuniorDeveloper. For PythonProgrammer3's instances, we have to pass in first name, last name only, but for Junior Developer, now we have to pass in salary as well
- We can use the class name ```PythonProgrammer3``` instead of ```super()``` as well, however, it is a better practice to use ```super()```. What it does is that, it will call the ```__init__()``` method from the parent class, and pass in the arguments that the parent class has, which is first name and last name. Then it will create new argument of its own, salary.
- Other way of doing this, is to copy the ```__init__()``` method from the parent class and paste it replacing the ```super()```. **This is not recommended**


```python
class JuniorDeveloper(PythonProgrammer3):
    def __init__(self, first, last, salary):
        super().__init__(first,last)
        self.salary = salary
```


```python
ju_dev_2 = JuniorDeveloper("Johan","Doe", 3000)
```


```python
ju_dev_2.__dict__
```




    {'first_name': 'Johan',
     'last_name': 'Doe',
     'email': 'Johan.Doe@python.com',
     'salary': 3000}




```python
# it's throwing an error because, now the JuniorDeveloper class, even though inherited from PythonProgrammer3
# it has its own way of instantiate/create new instance, and therefore, we have 1 argument missing.
# In order to fix it, we can modify the mothod from_string, by redefining it. 
# Try to see if you can do it yourself first !
ju_dev_3 = JuniorDeveloper.from_string('Johan-Doer')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-85-a5e97ac95286> in <module>
          3 # In order to fix it, we can modify the mothod from_string, by redefining it.
          4 # Try to see if you can do it yourself first !
    ----> 5 ju_dev_3 = JuniorDeveloper.from_string('Johan-Doer')
    

    <ipython-input-56-30d2ebc77273> in from_string(cls, string)
         25     def from_string(cls, string):
         26         first_name, last_name = string.split('-')
    ---> 27         return cls(first_name, last_name)
         28 
         29     @staticmethod


    TypeError: __init__() missing 1 required positional argument: 'salary'



```python
ju_dev_4 = JuniorDeveloper.from_string('Johan-Doer',3000)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-86-2f147683d006> in <module>
    ----> 1 ju_dev_4 = JuniorDeveloper.from_string('Johan-Doer',3000)
    

    TypeError: from_string() takes 2 positional arguments but 3 were given



```python
# My way of doing it
class JuniorDeveloper2(PythonProgrammer3):
    def __init__(self, first, last, salary):
        super().__init__(first,last)
        self.salary = salary
    
    @classmethod
    def from_string(cls, string,salary):
        first_name, last_name = string.split('-')
        return cls(first_name, last_name, salary)
```


```python
ju_dev_5 = JuniorDeveloper2.from_string('Johan-Doer',3000)
```


```python
ju_dev_5.__dict__
```




    {'first_name': 'Johan',
     'last_name': 'Doer',
     'email': 'Johan.Doer@python.com',
     'salary': 3000}




```python

```
