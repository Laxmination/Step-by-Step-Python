# Object Oriented Programming in Python

To map with real world scenarios, we started using objects in code. This is called <b>Object oriented programming.</b>

## Python Classes/Objects
Python is an object oriented programming language.<br>
Almost everything in Python is an object, with its properties and methods.<br>
A Class is like an object constructor, or a "blueprint" for creating objects.

### Class and instance Attributes
The data /variables that are stored inside the class or object are attributes.<br>
The precedence of object attribute is more than class attribute.<br>
Class.attr<br>
obj.attr

### __ _init_ __() Function

To understand the meaning of classes we have to understand the built-in __ _init_ __() function.<br>
All classes have a function called __ _init_ __(), which is always executed when the object is being initiated.<br>
<i>The __ _init_ __() function is called automatically everytime the class is being used to create a new object.</i>

### The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.<br>
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.