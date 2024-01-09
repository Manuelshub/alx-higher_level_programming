0x0A Python Inheritance
Description
This project explores the concept of inheritance in Python. Inheritance is a powerful feature that allows a new class to inherit attributes and methods from an existing class. Understanding inheritance is fundamental to creating well-organized and efficient Python code.

Project Structure
The project includes the following files:

[0-lookup.py](./0-lookup.py): A Python script that defines a function lookup(obj) to return a list of available attributes and methods of an object.

[1-my_list.py](./1-my_list.py): A Python class MyList that inherits from the list class. It adds a new method print_sorted() to print the list in ascending order.

[2-is_same_class.py](./2-is_same_class.py): A Python script that defines a function is_same_class(obj, a_class) to check if an object is an instance of a specified class.

[3-is_kind_of_class.py](./3-is_kind_of_class.py): A Python script that defines a function is_kind_of_class(obj, a_class) to check if an object is an instance of a class or a class that inherited from.

[4-inherits_from.py](./4-inherits_from.py): A Python script that defines a function inherits_from(obj, a_class) to check if an object is an instance of a class that inherited from the specified class.

[5-base_geometry.py](./5-base_geometry.py): An empty Python class BaseGeometry.

[6-base_geometry.py](./6-base_geometry.py): A Python class BaseGeometry with an instance method def area(self): that raises an exception. This serves as a base class for further development.

[7-base_geometry.py](./7-base_geometry.py): Additional functionality added to the BaseGeometry class with validations for integer values.

[8-rectangle.py](./8-rectangle.py): A Python class Rectangle that inherits from BaseGeometry. It includes additional attributes and methods to represent a rectangle.

[9-rectangle.py](./9-rectangle.py): A Python class Rectangle with additional validations for the width and height attributes.

[10-square.py](./10-square.py): A Python class Square that inherits from Rectangle. It represents a square and includes validations for the size attribute.
