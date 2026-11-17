#%%
#========================
#EXERCISE 1
# Create a tuple with days of the week
# Print the second and third day
# Traverse the elements and print
#========================
days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print(f"The second day is {days[1]}")
print(f"The third day is {days[2]}")
for i in days:
    print(i)
#%%
#========================
#EXERCISE 2
# With the tuple numbers:
# traverse and print only the even numbers.
# Traverse and print oly the odd numbers.
#========================
numbers = (1,8,9,44,55,98,102,117)
print("EVEN NUMBERS:")
for i in numbers:
    if i % 2 == 0:
        print(i)
print("\nODD NUMBERS:")
for i in numbers:
    if i % 2 != 0:
        print(i)
# %%
#========================
# EXERCISE 3
# With the tuple employees:
# Print the name of the employer with the highest salary.
# Print the name of the employer with the lowest salary.
# Traverse the collection and add only the names to a list, After, print the list.
# Traverse the collection and add only the salaryes to a list, After, print the list.
#========================
employees =(("Ana",3500),("Carlos",4200),("Beatriz",3900),("Daniel",5000))
print(f"The employer with the highest salary is:{max(employees)[0]}")
print(f"The employer with the lowest salary is:{min(employees)[0]}")
names = []
salaryes = []
for i in employees:
    names.append(i[0])
    salaryes.append(i[1])
print(names)
print(salaryes)

# %%
#========================
# EXERCISE 4
# With the tuple products
# Traverse the tuple and print the products with quantity greater than 10
# Traverse the tuple and print only the name of the products value greater then 200R$
# Traverse the tuple and print the sum of the all value products
# Traverse the tuple and print the total quantity of the products
#========================
products = (("Notebook", 3500.00, 10),("Mouse", 80.00, 50),("Teclado", 150.00, 30),("Monitor", 1200.00, 8),("Cadeira Gamer", 900.00, 5))
print("PRODUCTS WITH QUANTITY GREATER THAN 10:")
for i in products:
    if i[2] > 10:
        print(i[0])
print("\nPRODUCTS WITH VALUE GREATER THAN 200R$:")
for i in products:
    if i[1] > 200:
        print(i[0])
print("\nSUM OF THE ALL PRODUCTS:")
sum1=0
for i in products:
    sum1 += i[1]
print(sum1)
print("\nQUANTITY TOTAL:")
total=0
for i in products:
    total += i[2]
print(total)

