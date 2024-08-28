
#   Write a Python program that determines if a given year is a leap year or not.
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#python program to finde largest among three numbers

# Input three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Find the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}")

#python program to check if a number is positive or, negative or 0
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#A transport company

# Input distance
distance = float(input("Enter the distance traveled (in km): "))


# Calculate fare based on distance
if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = distance * 10
else:
    fare = distance * 12

print(f"The fare for {distance} km is Rs {fare}")

#A toy vender

# Input product code and order amount
product_code = int(input("Enter the product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
order_amount = float(input("Enter the order amount (in Rs): "))

# Calculate the net amount after applying discounts
if product_code == 1:  # Battery Based Toys
    if order_amount > 1000:
        discount = 0.10
    else:
        discount = 0.0

elif product_code == 2:  # Key-based Toys
    if order_amount > 100:
        discount = 0.05
    else:
        discount = 0.0

elif product_code == 3:  # Electrical Charging Based Toys
    if order_amount > 500:
        discount = 0.10
    else:
        discount = 0.0

else:
    print("Invalid product code")
    discount = 0.0

# Calculate final amount after discount
discounted_amount = order_amount * (1 - discount)

print(f"The net amount to be paid after discount is Rs {discounted_amount:.2f}")
