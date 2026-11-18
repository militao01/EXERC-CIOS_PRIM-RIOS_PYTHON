#%%
###### STEP 1: LIST COMPREHENSION ######
#==================================
# EXERCISE 1
# whith the list celsius, convert degrees Celsius(°C) to Fahrenheit(°F)
# Use the list comprehension
#==================================
celsius = [0, 10, 20, 25, 30, 40]
fahrenheit = [(i *1.8) + 32 for i in celsius]
print(fahrenheit)
# %%
#==================================
# EXERCISE 2
# with the list below, Create a new list containig the numbers greater than 10
#==================================
list1 = [3, 11, 7, 20, 5, 14, 2, 30]
new_list = [i for i in list1 if i >10]
print(new_list)
# %%
#==================================
# EXERCISE 3
# Using the setence, create a new list with only vowels
#==================================
sentence = "UNIFEI pouso alegre"
sentence_vowels = [i for i in sentence if i in "AaEeIiOoUu"] 
print(sentence_vowels)
# %%
###### STEP 2: DICT COMPREHENSION ######
#==================================
# EXERCISE 4 
# Using the list below, create a dictionary that the key is word and the value is the number of characters
#==================================
listA = ["Python", "dados", "código", "UNIFEI", "computação"]
dict1 = {word: len(word) for word in listA}
print(dict1)
# %%
#==================================
# EXERCISE 5
# Using the list below, create a new dict:
# - kew is the number
# - value is the string pair or odd
# - with olny number greater than 5
#==================================
listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict2 = {number:"pair" if number % 2 ==0 else "odd"  for number in listB if number >5}
print(dict2)
# %%
###### STEP 3: SET COMPREHENSION ######
#==================================
# EXERCISE 6
# Using the list below:
# - remove the duplicates 
# - remove less than 11
#==================================
listC = [5, 8, 8, 10, 12, 12, 14, 15, 18, 18, 20, 20, 20, 21]
set1 = {number for number in listC if number > 10}
print(set1)
# %%
#==================================
# EXERCISE 7
# Using the string below:
# Create a set without spaces
#==================================
string = "UNIFEI POUSO ALEGRE"
set2 = {i for i in string if i != " "}
print(set2)
