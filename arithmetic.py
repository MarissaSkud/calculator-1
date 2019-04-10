"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    added = num1 + num2
    return added


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    sub = num1 - num2
    return sub

def multiply(num1, num2):
    """Multiply the two inputs together."""
    product = num1 * num2
    return product

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    divided = num1 / num2 
    return divided 

def square(num1):
    """Return the square of the input."""
    squared = num1 * num1 
    return squared


def cube(num1):
    """Return the cube of the input."""
    cubed = num1 * num1 * num1 
    return cubed 


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    powered = num1 ** num2
    return powered

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    remainder = num1 % num2
    return remainder
