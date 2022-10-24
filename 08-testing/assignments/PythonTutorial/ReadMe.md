# Basic Tutorial

Make sure you have python installed. You can install it by going here:

[https://www.python.org/downloads/]

Run any file by doing:

`python filename.py`

## 1. HelloWorld.py

This simply stores "Hello World" in a string and then prints it.

## 2. Dictionary.py

This file shows how to user a dictionary object in python. A dictionary allows you to access each
element by a given name rather than an index.

It starts off by showing a simple dictionary example for favorite colors. You can access each by type the variable name
following by brackets with the key:

`exampleVariable['KEY']`

Next it shows you how to add a new key in the dictionary. You can simply do:

`exampleVariable['NEWKEY'] = newValue`

Lastly, it shows you how to create a dictionary of a dictionary. To access elements in this you simply do:

`exampleVariable['FIRSTKEY']['SECONDKEY']`

## 3. JSONFILES.PY

This file show you how to read and write to a json file. It uses the same dictionary as before. Dictionaries can easily 
be written to json files in python. First it writes a json files, then it reads it into a new dictionary.

## 4. Classes.py

This file shows how to uses classes and functions in python. In python when using classes you need to use 
`if __name__ == "__main__":` to run the code you want to execute.

This file creates a car and vehicle class. The car class inherits from the vehicle class. In the main statement it then
creates a car object and stores it in mustang.

## Classes Directory

This directory is the same as the classes file just spread across different files. You need to import any outside files 
into your program to access them. The main.py file contains the main program that is loaded.

### Example_test.py

First you need to install pytest:

`pip3 install pytest`

This file contains an example of a python test. The python test file must contain the '_test' or 'test_'. To run a pytest 
file write in terminal `pytest` to run all pytest files or `pytest filename` to run a specific test.