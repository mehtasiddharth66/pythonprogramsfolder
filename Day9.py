1. #Count all letters, digits, and special symbols
s = "P@yt9n26at&l5ve"
chars = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
symbols = len(s) - chars - digits
print(f"Chars = {chars} Digits = {digits} Symbols = {symbols}")
   

2. #Remove duplicate characters from a given string
s = "String and String Function"
result = "".join(sorted(set(s), key=s.index))
print(result)
   

3. #Count Uppercase, Lowercase, special characters, and numeric values
s = "Hell0 W0rld ! 123 # welcome to pYtHoN"
upper = sum(c.isupper() for c in s)
lower = sum(c.islower() for c in s)
digits = sum(c.isdigit() for c in s)
symbols = len(s) - upper - lower - digits
print(f"UpperCase: {upper}\nLowerCase: {lower}\nNumberCase: {digits}\nSpecialCase: {symbols}")
   

4. #Count vowels in a string
s = "Welcome to Python Assignment"
vowels = sum(c.lower() in 'aeiou' for c in s)
print(f"Total vowels are: {vowels}")