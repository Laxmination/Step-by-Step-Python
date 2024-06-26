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

## Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

### The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

### Additional Note
<i>We can modify properties on objects and we can also delete objects.</i>

## Static Method
Method that don't use the self parameter(work at class level)<br>
to create static method we use @staticmethod as decorator.<br>
Decorators allow us to wrap another function in order to expand the behaviour of the wrapped function, without permanently modifying it.

# Abstraction
Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation
Wrapping data and functions into a single unit(object).


## Private(like) attributes and methods
<b>Conceptual Implementations in Python</b>
Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.

# Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from class. i.e. when one class(child/derived) derives the properties and methods of another class(parent/base), then it is called inheritance.<br><br>
<b>Parent class:</b> It is the base class from which other class are derived.<br>
<b>Child class:</b> It is the derived class that inherits from another class i.e. inherits from parent class.<br>

### Types of Inheritance
1. Single Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance

### Super method
super() method is used to access methods of the parent class

## class method
A class method is bond to the class and receives the class as an implicit first argument. We use @classmethod as a decorator in class method.<br><br>

Note: static method cannot access or modify class state and generally for utility.

### Property
We use @property decorator on any method in the class to use the method as a property.

## Polymorphism
Polymorphism means many forms i.e. in Programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.<br><br>
Operator overloading is an exam of polymorphism and we say operator overloading if the same operator is allowed to have different meaning according to the context.