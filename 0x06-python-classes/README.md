# 0x06 Python Classes

This repository contains solutions to tasks related to Python classes.

## Tasks

### [0. My first square](./0-square.py)

Write an empty class `Square` that defines a square.

### [1. Square with size](./1-square.py)

Write a class `Square` that defines a square by using the `__init__` method to initialize the `size` attribute.

### [2. Size validation](./2-square.py)

Enhance the `Square` class by adding a private instance attribute `size` and implementing its getter and setter.

### [3. Area of a square](./3-square.py)

Add a public method `def area(self):` to the `Square` class that returns the current square area.

### [4. Access and update private attribute](./4-square.py)

Add a property `def size(self):` to retrieve the size and a setter `def size(self, value):` to set the size.

### [5. Printing a square](./5-square.py)

Add a public instance method `def my_print(self):` to the `Square` class to print the square using the `#` character.

### [6. Coordinates of a square](./6-square.py)

Add private instance attributes `position` with a default value of `(0, 0)` and implement a setter and getter for it.

## Usage

To test or use the classes provided in this repository, you can create instances of the `Square` class and call its methods.

Example:

```python
# Create a square with size 5
my_square = Square(5)

# Print the square
my_square.my_print()

# Get the area of the square
area = my_square.area()
print("Area:", area)

