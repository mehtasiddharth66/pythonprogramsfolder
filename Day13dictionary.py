#1)Write a Python program and calculate the mean of the below dictionary, test_dict = {"A": 6, "B": 9, "C": 5, "D" : 7, "E":4}


test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean = sum(test_dict.values()) / len(test_dict)
print("Mean:", mean)



#2)Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", result)

#3)Write a Python program to get the key, value and item in a dictionary.

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("Keys:", list(dict_num.keys()))

print("Values:", list(dict_num.values()))

print("Items:", list(dict_num.items()))

#4)Write a Python program to get the key, value and itern in a dictionary.

input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

print("Keys:", list(input_dict.keys()))

print("Values:", list(input_dict.values()))

print("Items:", list(input_dict.items()))
