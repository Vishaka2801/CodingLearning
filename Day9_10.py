# loop questions

# Print the elements of the following list using a loop :
# [1,4,9,16,25,36,4[9,64,81,100]
def problem_1():

    nums = [1,4,9,16,25,36,49,64,81,100]

    idx = 0 
    while idx< len(nums):   
        print(nums[idx])
    idx+=1 


# Search for a number x in this tuple using loop :
# (1,4,9,16,25,36,49,64,81,100)
def problem_2():

    nums = (1,4,9,16,25,36,49,64,81,100)

    x = 36
    i = 0 #initialization
    while i< len(nums):
        if (nums[i] == x):
            print ("Found idx" , i )

        else:
             print("finding")

        i+=1

#Break eg same 
def problem_3():

    nums = (1,4,9,16,25,36,49,64,81,100)

    x = 36
    i = 0 #initialization
    while i< len(nums):
        if (nums[i] == x):
                print ("Found idx" , i )
                break
        else:
             print("finding")
        i+=1

# Continue eg
def problem_4():
     i = 0
     while i <=5:
        if (i ==3):
            i +=1
            continue #skip
        print(i)
        i +=1

# for loop eg 
def problem_5():
    nums = [1,2,3,4,5]

    for val in nums :
        print(val)

# Print the elements of the following list using the loop :
# [1,4,9,16,25,36,49,64,81,100]
def problem_6() :

    nums = [1,4,9,16,25,36,49,64,81,100]
    for el in nums :
        print(el) 

# Search for a number x in this tuple using loop and print length as 
# well for x 
#[1,4,9,16,25,36,49,64,81,100]

def problem_7():

    nums = (1,4,9,16,25,36,49,64,81,100)
    x = 49
    idx = 0 

    for el in nums:
        if el == x:
            print("Found" , x ,"at index" , idx)
        idx += 1

# range eg
def problem_8():
    seq = range(5)

    for i in seq:
        print(i)


# range conditon eg
def problem_9 ():
    for i in range(10):  #range stop
        print (i)

        for i in range(2,10): #range start,stop
            print(i)

            for i in range (2,10,2): #range start,stop,step
                print(i)


# print even numbers
def problem_10 ():

    for i in range (2,  100, 2):
        print(i)

#practice

# Print numbers from 1 to 100 
def problem_11 ():

    for i in range (1, 101):
        print(i)

#print the multiplication table of a number n 
def problem_12():

    n = int(input("Enter number :"))
    for i in range (1,11):

        print(n*i)

#pass statement
def problem_13():
    
    for i in range(5):
        pass         #used as a null statement

    print ("Vishaka is best")

# practice
# to find sum of first n natural numbers (using for)
def problem_14():

    n = 5 
    sum = 0 
    for i in range (1, n+1):
        sum +=i
    print("total sum = ", sum)


# same while
def problem_15():
    
    n = 5 
    sum = 0 
    i = 1 
    while i<=n :
        sum +=i 
        i+=1
    print ("total sum =", sum)



#to find factotial of first n number (using for )
def problem_16():

    n = 5 
    fact = 1 
    i = 1 
    while i <=n:
        fact*= i 
        i +=1 
    print("factorial =" , fact)


     

    










#output area :
#problem_1() 
#problem_2()
#problem_3()
#problem_4()
#problem_5()
#problem_6 ()
#problem_7()
#problem_8()
#problem_9()
#problem_10()
#problem_11()
#problem_12()
#problem_13()
#problem_14()
#problem_15()
problem_16()