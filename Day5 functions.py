#Ans1 Declare a div()

# Define the div function
def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Call the function with two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = div(num1, num2)

print(f"The result of dividing {num1} by {num2} is: {result}")

#Ans2 Declare a square()

# Define the square function
def square(x):
    return x * x

# Call the function with a number and display the result
number = 5  # Example number
print(f"The square of {number} is: {square(number)}")


