#1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f'Result: {result}')

divide_numbers(10, 0)  # This will handle the division by zero
divide_numbers(10, 2)  # This will show the result of the division

#2 Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer():
    user_input = input("Please enter an integer: ")
    try:
        number = int(user_input)
        print(f'You entered: {number}')
    except ValueError:
        print("Error: Input is not a valid integer.")

get_integer()

#3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def open_file(filename):
    try:
        with open(filename) as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

open_file("example.txt")

#4 Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f'You entered: {num1} and {num2}')
    except ValueError:
        raise TypeError("Error: Both inputs must be numerical values.")

get_numbers()


