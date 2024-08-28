#1)Write a Python program to sum all the items in a list.
 #python short and good program
 
print(sum([1, 2, 3, 4, 5]))

#2)Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 
# Original list: ['red', 'green', 'white', 'black') Traverse the said list in reverse order: black white green red

colors = ['red', 'green', 'white', 'black']
for i in range(len(colors)-1, -1, -1):
    print(i, colors[i])
    

#3)Write a Python program to get the largest and smallest number from a list without builtin functions.

numbers = [4, 7, 1, 9, 3]
smallest = largest = numbers[0]

for num in numbers[1:]:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest:", smallest, "Largest:", largest)


#4)Write a Python program to find duplicate values from a list and display those.

numbers = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []

for i in range(len(numbers)):
    if numbers[i] in numbers[i+1:] and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

print("Duplicates:", duplicates)


#5)Write a Python program to split a given list into two parts

numbers = [1, 1, 2, 3, 4, 4, 5, 1]
n = 3
part1, part2 = numbers[:n], numbers[n:]
print((part1, part2))
