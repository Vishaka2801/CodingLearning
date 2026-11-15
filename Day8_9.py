# Python Practice 10 Questions

# 1 Number Calculator: Ask the user for two numbers. Print their addition, subtraction, multiplication, division and remainder.
def problem_1():
    print("Problem 1")
    a = float (input("Enter first number "))
    b = float (input("Enter second number "))
    task = (input("Enter task Add/subtract/multiply/divide : "))

    if task == "Add" :
        print ("Result:" , a+b)

    elif task == "subtract" :
        print ("Result:" , a-b)

    elif task == "multilpy" :
        print ("Result: ", a * b)

    elif task == "divide" :
        print ("Result: ",a / b )
        print("Remainder:", a % b)



# 2 Age Checker: Ask the user for their age. Print whether they are a child (below 13), teenager (13–19) or adult (20+).
def problem_2():
    print("Problem 2")

    a = int (input("Enter age"))

    if a < 13 :
        print("child")

    elif a >= 13 and a <= 19:
        print("teeneager")

    else :
        print("adult")



# 3 String Analyser: Ask the user for their full name. Print its uppercase, lowercase, length, first character and last character.
def problem_3():
    print("Problem 3")

    a = (input ("Enter full name "))
    print(a.upper())
    print(a.lower())
    print(len(a))
    print(a[0])
    print(a[-1])



# 4 Shopping List: Create a list of five products. Add two products, remove one product, change one product and print the final list.
def problem_4():
    print("Problem 4")

    list = [ "apple" , "mango" , "kiwi" , "melon" , "berry"]
    list.append("grapes")
    list.append("chiku")
    print(list)

    list.remove("berry")
    print(list)

    list[1] = "orange"
    print(list)

# 5 Duplicate Remover: Given the list below, convert it into a set and print the unique values.
def problem_5():

    numbers = [10, 20, 10, 30, 40, 20, 50, 30]

    print(set(numbers))


# 6 Student Record: Create a dictionary containing a student's name, age, course and marks. Update their marks and add their university.
def problem_6():

    a = { 
        
        "name" : "Vishaka" ,
        "age" : 22 , 
        "course" : "Computer Science" ,
        "marks" : 80

}
    a["university"] = "Harvard"
    print(a)

    a.update ({"marks" : 85})
    print(a)



#7 Create a tuple of five countries. Print the second and fourth countries, the total number of countries and try changing one country.
def problem_7():

    a = ("India" , "Canada" , "Spain" , "Australia" , "Germany")
    print(a[2])
    print(a[4])
    print(len(a))

    y = list(a)
    y.append("Mumbai")
    a = tuple(y)
    print(a)


    #8 Positive, Negative or Zero: Ask the user to enter a number. Determine whether it is positive, negative or zero. 
    #If it isn't zero, also determine whether it is even or odd.
def problem_8():

    a = int(input("Enter a number ") )

    if a == 0 :
        print(0)

    else:
        if a > 0 :
            print("positive")


        if a % 2 == 0 :
            print ("even")
        else : 
            print ("odd")

    if a < 0 :
        print ("negative")



# 9 Grading System: Ask the user for marks between 0 and 100. Assign grades A, B, C, D or Fail. Display an error for invalid marks.
def problem_9():

    a = float(input("Enter marks "))

    if a <0 or a >100 :
        print("Invalid Marks")

    elif a >=90 :
        print("A grade")

    elif a>= 80:
        print ("B grade")

    elif a>= 70 :
        print("C grade")

    elif a>= 60:
        print ("D grade")

    else:
        print("fail")



# 10 Start with a balance of £1,000. Ask the user whether they want to deposit, withdraw or check their balance. 
# Perform the selected operation and prevent withdrawals exceeding the available balance.
def problem_10():

    balance  = 1000 

    task = input ("Enter task, deposit / withdraw /check their balance.  ")







#Code challenge for loops

# 11 Print numbers from 1 to 100 
def problem_11 ():

    i = 1
    while  i <= 100:
        print(i)
        i +=1

# 12 Print the multiplication table for a number n
def problem_12 ():

    n = int(input("Enter number "))
    i = 1
    while i <= 10 :
        print(n*i)
        i +=1


























#Output area:
# problem_1()
# problem_2()
# problem_3()
# problem_4()
#problem_5 ()
#problem_6 ()
#problem_7 ()
#problem_8 ()
#problem_9 ()
#problem_10 ()
#problem_11 ()
problem_12()




