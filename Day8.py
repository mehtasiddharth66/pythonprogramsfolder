#1 Write a Python program to count the occurrences

import string as str_lib
from collections import Counter

sentence = "To change the overall look of your document. To change the look gallery"

# Convert to lowercase, remove punctuation, and split into words
words = sentence.lower().translate(str_lib.maketrans('', '', str_lib.punctuation)).split()

# Count occurrences of each word
word_count = Counter(words)

# Print the word counts
for word, count in word_count.items():
    print(f'{word}: {count}')
    
#2 Write a Python program to remove a newline in Python

string = "inBest\ninDeeptech\nPython\nTrainingin"

# Remove newline characters by splitting and joining
cleaned_string = ''.join(string.splitlines())

print(cleaned_string)

#3 Write a Python program to reverse words in a string String Deeptech Python Training

string = "Deeptech Python Training"

# Split the string into words
words = string.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed list back into a string
reversed_string = ' '.join(reversed_words)

print(reversed_string)

#4 Write a Python program to count and display the vowels of a given text StringWelcome to python Training

text = "Welcome to python Training"

# Define vowels
vowels = 'aeiou'

# Convert the text to lowercase for uniformity
text_lower = text.lower()

# Initialize a dictionary to count vowels
vowel_count = {vowel: 0 for vowel in vowels}

# Count occurrences of each vowel
for char in text_lower:
    if char in vowel_count:
        vowel_count[char] += 1

# Display the counts of each vowel
for vowel, count in vowel_count.items():
    print(f'{vowel}: {count}')



