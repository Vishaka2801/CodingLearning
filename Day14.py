# Question 1 — Lists + Loops

# Write a Python program that:
# 1. Creates a list containing 5, 10, 15, 20, 25.
# 2. Uses a for loop to go through the list.
# 3. Prints each number multiplied by 2

numb = [5, 10, 15, 20, 25]
for x in numb:
    print(x*2)


# Question 2 — Lists + While Loops
# Create a program that:
# 1. Creates a list containing five numbers.
# 2. Uses a while loop to print each number.
# 3. Prints the numbers in reverse order.
# Example list: [10, 20, 30, 40, 50]

def problem_2():
    num = [10, 20, 30, 40, 50]

    i = len(num)-1
    i = 4
    while i >=0:
        print ((num)[i])
    i -=1 


# Print only the even numbers from a list.

# Given:
# numbers = [3, 8, 12, 5, 17, 20, 25, 30]

# Your task:
# 1. Use a for loop to go through the list.
# 2. Use if to check whether a number is even.
# 3. Print only the even numbers.

def problem_3 ():
    numbers = [3, 8, 12, 5, 17, 20, 25, 30]
    print (numbers)

    for x in numbers:
        if x%2 == 0:
            print (x)



