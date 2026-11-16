# %%
#===========================
# EXERCISE 1
# Create a set with 6 elements
# Add to new elements
# Remove one element from set
# Traverse the elements of the final set and print them
#============================
first_set = {0,2,4,6,8,10}
print(f"The original is {first_set}")
first_set.update([12,14])
first_set.remove(0)
print(f"The final set is {first_set}")
for x in first_set:
    print(x)

# %%
#===========================
# EXERCISE 2
# Start a list wtih 6 elements
# Change the list for set and print
#===========================
prime_list = [2,3,5,7,11,13]
prime_set = set(prime_list)
print(f"The resulting set is {prime_set}")

# %%
#===================================
# EXERCISE 3
# Ask to the user 7 numbers
# Put it in a list
# remove the duplicates and print
#===================================
list1 = []
for i in range(1,8):
    x = int(input(f"Type the {i}º number: "))
    list1.append(x)
print(list1)
set1 = set(list1)
print(f"The list of numbers without duplicates is:\n{set1}")
# %%
#===================================
# EXERCISE 4
# Start with 2 sets with 5 integers
# Show the union and the intersection between the sets
# Show the difference
# Show the symmetric difference
#===================================
set_A = {2,4,6,8,12}
set_B = {3,6,9,12,15}
print(f"The Union: {set_A.union(set_B)}")
print(f"The Intersection: {set_A.intersection(set_B)}")
print(f"The difference{set_A.difference(set_B)}")
print(f"The symmetric_difference:{set_A.symmetric_difference(set_B)}")
# %%
#===================================
# EXERCISE 5
# Start with 2 sets with 5 integers
# Check if all elements of a set are in other
# Check if a set contains all elements of other
# check if the number 10 is in some set
#===================================
A = {2,4,6,8,10,12}
B = {4,8,12}
print(f"Set A is subset of B:{A.issubset(B)}")
print(f"Set B is subset of A {B.issubset(A)} ")
print(f"Set A is superset of B:{A.issuperset(B)}")
print(f"Set B is superset of A {B.issuperset(A)} ")
print(f"The Number 10 is in Set A {10 in A}")
print(f"The Number 10 is in Set B {10 in B}")