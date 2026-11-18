# funtion continue qs

# 1 find factorial of n

def cal_fact(n) :
    fact =1
    for i in range (1, n+1):
        fact *= i
    print(fact)

cal_fact(7)


# 2 convert USD to INR 

def converter (usd_val):
    inr_val = usd_val * 83 
    print(usd_val , "USD =", inr_val, "INR")

converter(3)


#Recursion 
# When a func calls itself repeatedly 

def show(n):
    if (n ==0):
        return
    print(n)
    show(n-1)

show(5)



#calculate factorial of n 

def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact (n-1) * n 

print(fact(4))


# practice qs1 : write a recursive function to calculate sum of 
# first n natural num 

def cal_sum(n) :
    if (n ==0):
        return 0
    return cal_sum (n-1) + n 

sum =  cal_sum (7)
print (sum)





# write a recursive function to print all elements in  a list.
# hint : use list & index as parameters

def print_list(list, idx):
    if (idx == len(list)):
        return
    print (list[idx])
    print_list(list, idx + 1)

fruits = ["mango" , "apple" , "kiwi" , "grape"]

print_list(fruits,0)