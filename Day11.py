# function eg 

# function defination 
def calc_sum(a,b): # parameters 
    return a + b 

sum = calc_sum(1,2) # function call; arguments
print(sum)





# average of 3 numbers
def calc_avg (a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg (2,4,5)


# function pracice qs

# 1 print the length of a list   (list is the parameter)

cities = [ "Mumbai", "Pune" , "Alibaug" , "Nashik" , "Nagpur" , "Lonavala" ]

def print_len(cities):
    print(len(cities))



# 2 print elements of a list in a single line (list is the parameter)


colors = ["red", "blue", "grey", "purple"]

def print_list(colors):
    for item in colors:
        print(item, end=" ")


#outputs 
#print_len(cities)
#calc_avg
#calc_sum
print_list(colors)

