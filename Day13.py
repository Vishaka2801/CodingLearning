# Practice qs

# question 1: Number Analysis

# Write a Python program that:
# 1. Asks the user to enter 5 numbers.
# 2. Stores them in a list.
# 3. Prints the list.
# 4. Prints the total of all five numbers.



numbers = []
for i in range (5):
    a = int(input("Enter a number: "))
    numbers.append(a)
    print(numbers)
    print(sum(numbers))







#  Question 2 of 5 — Even and Odd Numbers

# Task:
# 1. Ask the user to enter 5 integers.
# 2. Store them in a list.
# 3. Use a for loop to go through the list.
# 4. Check whether each number is even or odd.
# 5. Print the result for each number.


for i in range (5):
    a = int (input("Enter a number "))
    if a % 2 == 0 :
        print ("even")

    else:
        print("odd")



# Question 3 of 5 — Find the Largest Number
# Task:
# 1. Ask the user to enter 5 numbers.
# 2. Store them in a list.
# 3. Find the largest number.
# 4. Print the largest number.


numbers = []

for i in range(5):
    a = int(input("Enter a number: "))
    numbers.append(a)

largest = max(numbers)

print("The largest number is:", largest)

