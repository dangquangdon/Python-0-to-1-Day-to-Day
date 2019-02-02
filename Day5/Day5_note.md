# Day 5

## Class methods(also see materials of day 4)
- use @classmethod decorator above your method to let python know that you are defining a class method
- class method take the class itself as the first argument, ```cls```
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
In this example code, we have two class
  - The first method ```set_language``` will change the class variable ```language```. It means that the it change in the class level, all of the objects that belong to this class will be affected.
  - Regular method ```speak``` only affects the a specific object that calls this method
  - The second class method ```from_string``` returns ```cls(first_name, last_name)``` which is the exact same syntax when we create new objects. E.g:
    ```python
    py_dev1 = PythonProgrammer3("Fistname", "Lastname")
    # In here, cls represents the class, which is PythonProgrammer3
    ```
  - By using ```from_string``` method, we can create new instance as well, from a different string format
  ```python
  py_dev2 = PythonProgrammer3.from_string("Firstname-Lastname")
  ```

  - In this case, ```from_string``` method is considered as an alternative constructor

**Static method (explained in day 4 material)**


## Pip (package manager)

- From now on, you will need to use pip to install extra packages quite often.
- If you installed Python3 from python.org as recommended before the course, pip is also installed, but if you install Python3 from other sources, you might not have it yet. If so, you can try this instruction

**Install pip in Windows:**
- [get_pip.py](https://bootstrap.pypa.io/get-pip.py)
- Create a new python file, and paste the code in it, then save it.
- In case you get confused with the steps above, just download/copy the get_pip.py file in this folder
- Open your command prompt, and use ``cd`` to navigate to the folder that contains get_pip.py
- run ```python get_pip.py``` or ```python3 get_pip.py```
- Let the installation finish
- Go to this [tutorial](https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/), scroll down and start from **Add PIP to the Windows Environment Variables**
- Notice that, in the tutorial, the python path ```C:\Python35\Scripts``` is just example, you should find the path of your python installed folder in your laptop. I can't be more specific than this since I can't tell everyone's laptop folders. I hope you can manage

**MacOS**

- This [tutorial](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/) is very specific.

**Ubuntu/Linux**

- It's very simple in ubuntu
- Open terminal and run ```sudo apt-get install python3-pip``` insert your user's password and wait for the installation to finish

**To check if pip is installed**
- open terminal or command prompt and type ```pip --version``` or ```pip3 --version```


## Virtualenv (virtual environment)

- Every project you are working on in the future will need to install and use different dependencies/packages. You will use ```virtualenv``` to create a virtual environment for each project so that they can be isolated and efficient.

- Imagine that your program is like a fish, depends on how you program it. If you are making a sea fish, you need to put it in an environment of sea water, and if you are making a fish living in a lake, you need the lake's water. If you install everything in your real environment which is your laptop, sea water and lake water will be mixed and it might affect the behavior of your fish, and also it will take more unnecessary laptop memories.

- Using virtualenv, technically, it is still in your laptop, but the enviroment is isolated and it's not connected with your real environments.

**Install with pip**
- Open Terminal or Command Prompt and run ```pip install virtualenv``` or ```pip3 install virtualenv```

**How to use**

- First of all, with every project you are going to work on, make sure you create a separate folder for it. And you are going to store all the python script of that project in that folder.

- After creating a new folder, open termnial or command prompt, use ```cd``` to navigate to that folder.

- Once you are inside that folder, run ```virtualenv venv```. Please note that, ```venv``` is , by convention, the name of the virtual environment folder, you can name it something else, for example ```virtualenv project_env``` or ```virtualenv my_virtual_env```

- After it finish runing virtualenv, you will see a new folder is created inside your project folder.

**For MacOs and Linux**
- run ```. venv/bin/activate``` or more friendly ```source venv/bin/activate```

**For Windows**
- run ```\venv\Scripts\activate``` or
- ``` cd venv/Scripts``` and then ```activate```. After that remember to ``cd..`` (maybe 2 times) to go back to your project folder

- If it's activated successfully, you will see something like this ```(venv) $....```

- To deactivate the virtual environment, simply type ```deactivate``` or just turn off the terminal or command prompt


